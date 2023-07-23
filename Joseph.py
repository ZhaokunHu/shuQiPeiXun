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


class DequeJosephus(deque):

    def __init__(self, total_number, step, people_list):
        self.total_number = total_number
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

    def __iter__(self):
        """使用迭代器来求解"""
        LogMaker.logger.info('使用迭代器来求解')
        self.iter_list = deepcopy(people_list)
        return self

    def __next__(self):
        if (len(self.iter_list) == 0):
            raise StopIteration
        id = (self.step-1) % len(self.iter_list)
        removed = self.iter_list[id]
        self.iter_list = self.iter_list[id:]+self.iter_list[:id]
        return removed

    def find_answer(self):
        """使用迭代器迭代对象"""
        for people in self:
            pass
        else:
            return people


if __name__ == "__main__":
    LogMaker.logger.info('程序开始运行')
    filename = 'JosephusCircle.zip'
    people_list = JosephReader.Reader().read_file(filename=filename)
    if (people_list == []):
        LogMaker.logger.error('文件名无效')
        raise ValueError('文件名无效')
    solution = AllMethods(total_number=len(people_list),
                          step=3, people_list=people_list)
    print("序号:{},姓名:{},年龄:{}".format(
        survival1.id, survival1.name, survival1.age))
    assert (survival1.id == survival2.id and survival1.id == survival3.id
            and survival1.id == survival4.id and survival1.id == survival5.id
            and survival1.id == survival6.id)
    LogMaker.logger.info('程序运行结束')
