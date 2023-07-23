from Joseph import Person
import csv
import zipfile
import LogMaker


class CsvReader:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as csv_file:
                csv_reader = csv.reader(csv_file)
            for line_content in csv_reader:
                id = line_content[0].split(':')[1].strip()
                name = line_content[1].split(':')[1].strip()
                age = line_content[2].split(':')[1].strip()
                self.people_list.append(Person(id, name, age))
        except FileNotFoundError:
            raise FileNotFoundError(f"Can't find '{self.filename}'")


class Reader:
    def __init__(self):
        self.people_list = []

    def read_txt(self, filename):
        LogMaker.logger.info('读取txt文件')
        with open(filename, 'r') as txt_file:
            line_content = txt_file.readline()
            while (line_content):
                id = line_content.split(',')[0].split(':')[-1].strip()
                name = line_content.split(',')[1].split(':')[-1].strip()
                age = line_content.split(',')[2].split(':')[-1].strip()
                self.people_list.append(Joseph.Person(id, name, age))
                line_content = txt_file.readline()

    def read_csv(self, filename):
        LogMaker.logger.info('读取csv文件')

    def read_file(self, filename):
        typename = filename.split('.')[1].strip()
        if (typename == 'txt'):
            self.read_txt(filename)
        elif (typename == 'csv'):
            self.read_csv(filename)
        elif (typename == 'zip'):
            LogMaker.logger.info('读取zip文件')
            with zipfile.ZipFile(filename, 'r') as zip_file:
                file_list = zip_file.namelist()
                self.read_file(file_list[0])
        else:
            pass
        return self.people_list
