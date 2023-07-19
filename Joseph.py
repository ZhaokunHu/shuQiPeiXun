import sys
import time
from copy import deepcopy
from collections import deque
import JosephReader
import LogMaker
sys.setrecursionlimit(1000000)


class Person:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age


class SolvingJosephMethods:
    def __init__(self, total_number, step, people_list):
        self.total_number = total_number
        self.step = step
        self.people_list = people_list

    def __iter__(self):
        """使用迭代器来求解"""
        LogMaker.logger.info('使用迭代器来求解')
        self.iter_list = deepcopy(people_list)
        return self

    def __next__(self):
        if (len(self.iter_list) == 0):
            raise StopIteration
        id = (self.step-1) % len(self.iter_list)
        removed = self.iter_list.pop(id)
        self.iter_list = self.iter_list[id:]+self.iter_list[:id]
        return removed

    def use_list(self):
        """使用list来进行求解"""
        LogMaker.logger.info('使用list来求解')
        person_list = deepcopy(people_list)
        list_counter = 0
        while (len(person_list) > 1):
            list_counter = (list_counter+self.step-1) % len(person_list)
            person_list.pop(list_counter)
        return person_list[0]

    def use_linkedlist(self):
        """使用链表来求解"""
        LogMaker.logger.info('使用链表来求解')
        linkedlist = LinkedList()
        for person in self.people_list:
            linkedlist.append(person)
        current = linkedlist.head
        step_counter = 0
        while (linkedlist.head != linkedlist.tail):
            step_counter += 1
            if (step_counter == self.step):
                step_counter = 0
                linkedlist.delete(current.data)
            current = current.next
        return linkedlist.head.data

    def use_deque(self):
        """使用collections库中的deque求解"""
        LogMaker.logger.info('使用collections库中的deque求解')
        queue = deque(self.people_list)
        while (len(queue) > 1):
            queue.rotate(1-self.step)
            queue.popleft()
        return queue[0]

    def use_ecursion1(self, total_number=None, step=None):
        """使用递归的方法进行求解"""
        if total_number is None:
            total_number = self.total_number
        if step is None:
            step = self.step
        if total_number == 0:
            return 0
        counter = self.use_ecursion1(total_number-1, step)
        if (total_number == self.total_number):
            LogMaker.logger.info('使用递归的方法进行求解')
            return people_list[(step+counter) % total_number]
        return (step+counter) % total_number

    def use_ecursion2(self):
        """使用递推的方法进行求解"""
        LogMaker.logger.info('使用递推的方法进行求解')
        counter = 0
        for i in range(2, self.total_number + 1):
            counter = (counter + self.step) % i
        return self.people_list[counter]


class LinkedList:
    class LinkedListNode:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = LinkedList.LinkedListNode(data)
        if (self.head is None):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.tail.next = self.head

    def delete(self, data):
        if (self.head is None):
            return
        if (self.head.data == data):
            if (self.head == self.tail):
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.tail.next = self.head
            return
        current = self.head
        prev = None
        while current:
            if (current.data == data):
                prev.next = current.next
                if (current == self.tail):
                    self.tail = prev
                return
            prev = current
            current = current.next


def data_input():
    while True:
        total_number = input("请输入总人数>")
        step = input("请输入间隔>")
        if (total_number.isdigit() and step.isdigit()
                and int(total_number) > 0 and int(step) > 0):
            return int(total_number), int(step)
        else:
            print("输入的数据应当为正整数")


def measure_time(func):
    start_time = time.perf_counter()
    solution = func()
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    return solution, execution_time


def use_iter():
    """使用迭代器迭代对象"""
    file_writer = open('JosephusAnswer.txt', 'w')
    for people in solution:
        file_writer.write("序号:{},姓名:{},年龄:{}\n".format(
            people.id, people.name, people.age))
    else:
        file_writer.close()
        return people


if __name__ == "__main__":
    LogMaker.logger.info('程序开始运行')
    filename = 'JosephusCircle.zip'
    people_list = JosephReader.Reader().read_file(filename=filename)
    if (people_list == []):
        LogMaker.logger.error('文件名无效')
        raise ValueError('文件名无效')
    solution = SolvingJosephMethods(total_number=len(people_list),
                             step=3, people_list=people_list)
    survival1, time1 = measure_time(solution.use_list)
    survival2, time2 = measure_time(solution.use_linkedlist)
    survival3, time3 = measure_time(solution.use_deque)
    survival4, time4 = measure_time(solution.use_ecursion1)
    survival5, time5 = measure_time(solution.use_ecursion2)
    survival6, time6 = measure_time(use_iter)
    print("序号:{},姓名:{},年龄:{}".format(
        survival1.id, survival1.name, survival1.age))
    print("数组方法的用时:{}\n链表方法的用时:{}\n队列方法用时:{}\n"
          "递归方法的用时:{}\n递推方法的用时:{}\n迭代器方法的用时:{}".format(
              time1, time2, time3, time4, time5, time6))
    assert (survival1.id == survival2.id and survival1.id == survival3.id
            and survival1.id == survival4.id and survival1.id == survival5.id
            and survival1.id == survival6.id)
    LogMaker.logger.info('程序运行结束')
