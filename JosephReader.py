from Joseph import Person
import csv
import zipfile
import os
from LogConfig import setup_logging
logger = setup_logging()


class TxtReader:
    def __init__(self, filename):
        self.filename = filename
        self.people_list = []

    def begin_read(self):
        logger.info('读取txt文件')
        try:
            with open(self.filename, 'r', encoding='utf-8') as txt_file:
                line_content = txt_file.readline()
                while (line_content):
                    id = line_content.split(',')[0].split(':')[-1].strip()
                    name = line_content.split(',')[1].split(':')[-1].strip()
                    age = line_content.split(',')[2].split(':')[-1].strip()
                    self.people_list.append(Person(id, name, age))
                    line_content = txt_file.readline()
            return self.people_list
        except FileNotFoundError:
            raise FileNotFoundError(f"Can't find '{self.filename}'")


class CsvReader:
    def __init__(self, filename):
        self.filename = filename
        self.people_list = []

    def begin_read(self):
        logger.info('读取csv文件')
        try:
            with open(self.filename, 'r', encoding='utf-8') as csv_file:
                csv_reader = csv.reader(csv_file)
                for line_content in csv_reader:
                    id = line_content[0].split(':')[1].strip()
                    name = line_content[1].split(':')[1].strip()
                    age = line_content[2].split(':')[1].strip()
                    self.people_list.append(Person(id, name, age))
            return self.people_list
        except FileNotFoundError:
            raise FileNotFoundError(f"Can't find '{self.filename}'")


class ZipReader:
    def __init__(self, filename):
        self.filename = filename
        self.people_list = []

    def begin_read(self):
        logger.info('读取zip文件')
        try:
            with zipfile.ZipFile(self.filename, 'r') as zip_file:
                file_names = zip_file.namelist()
                for file_name in file_names:
                    with zip_file.open(file_name, 'r') as file:
                        # 判断文件扩展名，如果是 '.txt' 文件则调用 TxtReader 处理
                        if file_name.endswith('.txt'):
                            reader = TxtReader(file_name)
                        # 如果是 '.csv' 文件则调用 CsvReader 处理
                        elif file_name.endswith('.csv'):
                            reader = CsvReader(file_name)
                        # 调用相应的 reader 处理内容，并将结果合并到 people_list
                        self.people_list = reader.begin_read()
            return self.people_list
        except FileNotFoundError:
            raise FileNotFoundError(f"Can't find '{self.filename}'")


def read_file(filename):
    typename = os.path.splitext(filename)[-1]
    if (typename == '.txt'):
        return TxtReader(filename).begin_read()
    elif (typename == '.csv'):
        return CsvReader(filename).begin_read()
    elif (typename == '.zip'):
        return ZipReader(filename).begin_read()
    else:
        raise FileNotFoundError(f"Don't support the typename of '{filename}'")
