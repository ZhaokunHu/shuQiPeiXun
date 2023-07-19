from collections import deque

class Person:
    def __init__(self, name):
        self.name = name

class JosephusCircle(deque):
    def __init__(self, persons):
        super().__init__(persons)

    def eliminate(self, k):
        print(len(self))
        self.rotate(-k)
        eliminated = self.pop()
        self.rotate(k - 1)
        return eliminated.name


persons = [Person("Alice"), Person("Bob"), Person("Charlie"), Person("David")]

# 创建新的Person对象进行深拷贝
copied_persons = [Person(person.name) for person in persons]

circle = JosephusCircle(copied_persons)
while len(circle) > 1:
    eliminated_name = circle.eliminate(2)
    print("Eliminated:", eliminated_name)