from Joseph import Person
import csv
import zipfile
import LogMaker


class TxtReader:
    def __init__(self, filename):
        self.filename = filename
        self.people_list = []

    def read_file(self, filename):

        LogMaker.logger.info('读取txt文件')
        try:
            with open(filename, 'r') as txt_file:
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

    def read_file(self):
        LogMaker.logger.info('读取csv文件')
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

    def read_file(self):
        LogMaker.logger.info('读取zip文件')
        try:
            with zipfile.ZipFile(self.filename, 'r') as zip_file:
                inner_file = zip_file.namelist()[0]
            return inner_file
        except FileNotFoundError:
            raise FileNotFoundError(f"Can't find '{self.filename}'")


def read_file(filename):
    typename = filename.split('.')[1].strip()
    if (typename == 'txt'):
        return TxtReader(filename).read_file()
    elif (typename == 'csv'):
        return CsvReader(filename).read_file()
    elif (typename == 'zip'):
        return read_file(ZipReader(filename).read_file())
    else:
        raise FileNotFoundError(f"Don't support the typename of '{filename}'")
