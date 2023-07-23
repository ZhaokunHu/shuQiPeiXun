from faker import Faker
import random
fake = Faker("zh_CN")
file_writer = open('JosephusCircle.txt', 'w')
for i in range(0, 1000):
    file_writer.write("序号:{},姓名:{},年龄:{}\n".format(
        i, fake.name(), random.randint(0, 100)))
file_writer.close()
