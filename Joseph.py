import sys
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


class DequeJosephus(deque):

    def __init__(self, step, people_list):
        self.step = step
        self.people_list = people_list
        super().__init__(people_list)

    def find_answer(self):
        """使用collections库中的deque求解"""
        LogMaker.logger.info('使用collections库中的deque求解')
        while (len(self) > 1):
            self.rotate(1-self.step)
            self.popleft()
        return self[0]


class IterJosephus:

    def __init__(self, step, people_list):
        self.step = step
        self.people_list = people_list
        self.iter_list = deepcopy(people_list)

    def __iter__(self):
        """使用迭代器来求解"""
        LogMaker.logger.info('使用迭代器来求解')
        return self

    def __next__(self):
        if (len(self.iter_list) == 0):
            raise StopIteration
        id = (self.step-1) % len(self.iter_list)
        removed = self.iter_list[id]
        self.iter_list = self.iter_list[id+1:]+self.iter_list[:id]
        return removed

    def find_answer(self):
        """使用迭代器迭代对象"""
        with open('JosephusAnswer.txt', 'w') as file_writer:
            for people in self:
                file_writer.write("序号:{},姓名:{},年龄:{}\n".format(
                    people.id, people.name, people.age))
            return people


if __name__ == "__main__":
    LogMaker.logger.info('程序开始运行')
    filename = 'JosephusCircle.zip'
    people_list = JosephReader.read_file(filename=filename)
    survival1 = DequeJosephus(3, people_list).find_answer()
    survival2 = IterJosephus(3, people_list).find_answer()
    print("序号:{},姓名:{},年龄:{}".format(
        survival1.id, survival1.name, survival1.age))
    assert (survival1.id == survival2.id)
    LogMaker.logger.info('程序运行结束')
