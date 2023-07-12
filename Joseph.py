import sys
import time
from collections import deque
sys.setrecursionlimit(1000000)


class Person:
    def __init__(self, number, name, age=20):
        self.number = number
        self.name = name
        self.age = age


class Methods:
    def __init__(self, total_number, step, people_list):
        self.total_number = total_number
        self.step = step
        self.people_list = people_list
        self.iter_list = [people for people in people_list]

    def __iter__(self):
        return self

    def __next__(self):
        """使用迭代器来求解"""
        if (len(self.iter_list) == 0):
            raise StopIteration
        idx = (self.step-1) % len(self.iter_list)
        removed = self.iter_list.pop(idx)
        self.iter_list = self.iter_list[idx:]+self.iter_list[:idx]
        return removed

    def use_list(self):
        """使用list来进行求解"""
        person_list = [person for person in people_list]
        list_counter = 0
        while (len(person_list) > 1):
            list_counter = (list_counter+self.step-1) % len(person_list)
            person_list.pop(list_counter)
        return person_list[0]

    def use_linkedlist(self):
        """使用链表来求解"""
        linkedlist = LinkedList()
        for person in self.people_list:
            linkedlist.append(person)
        current = linkedlist.head
        step_counter = 0
        while (linkedlist.head != linkedlist.tail):
            step_counter += 1
            if (step_counter == step):
                step_counter = 0
                linkedlist.delete(current.data)
            current = current.next
        return linkedlist.head.data

    def use_deque(self):
        """使用collections库中的deque求解"""
        queue = deque(self.people_list)
        while (len(queue) > 1):
            queue.rotate(1-step)
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
            return people_list[(step+counter) % total_number]
        return (step+counter) % total_number

    def use_ecursion2(self):
        """使用递推的方法进行求解"""
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


def create_list(total_number):
    people_list = []
    for i in range(0, total_number):
        one_person = Person(number=i, name='_-%d' % (i)+'-_')
        people_list.append(one_person)
    return people_list


def measure_time(func):
    start_time = time.perf_counter()
    solution = func()
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    return solution, execution_time


if __name__ == "__main__":
    total_number, step = data_input()
    people_list = create_list(total_number)
    solution = Methods(total_number=total_number,
                       step=step, people_list=people_list)
    survival1, time1 = measure_time(solution.use_list)
    survival2, time2 = measure_time(solution.use_linkedlist)
    survival3, time3 = measure_time(solution.use_deque)
    survival4, time4 = measure_time(solution.use_ecursion1)
    survival5, time5 = measure_time(solution.use_ecursion2)
    print("序号:{},姓名:{},年龄:{}".format(
        survival1.number, survival1.name, survival1.age))
    print("数组方法的用时:{}\n链表方法的用时:{}\n队列方法用时:{}\n递归方法的用时:{}\n递推方法的用时:{}".format(
        time1, time2, time3, time4, time5))
    assert (survival1 == survival2 and survival1 == survival3
            and survival1 == survival4 and survival1 == survival5)
    file_writer = open('JosephusCircle.txt', 'w')
    for people in solution:
        file_writer.write("序号:{},姓名:{},年龄:{}\n".format(
            people.number, people.name, people.age))
