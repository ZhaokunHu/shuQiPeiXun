import JosephReader
import Joseph
import unittest


class UnittextJoseph(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.people_list = JosephReader.read_file('JosephusCircle.txt')
        cls.name_list = [people.name for people in cls.people_list]

    def setUp(self):
        pass

    def text_deque_find_answer(self):
        survival = Joseph.DequeJosephus(3, self.people_list).find_answer()
        self.assertEqual(survival.id, '2691')

    def text_iter_find_answer(self):
        survival = Joseph.IterJosephus(3, self.people_list).find_answer()
        self.assertEqual(survival.id, '2691')

    def text_txt_reader(self):
        peoson_list = JosephReader.TxtReader('JosephusCircle.txt').begin_read()
        txt_name_list = [person.name for person in peoson_list]
        self.assertListEqual(txt_name_list, self.name_list)

    def text_csv_reader(self):
        peoson_list = JosephReader.CsvReader('JosephusCircle.csv').begin_read()
        csv_name_list = [person.name for person in peoson_list]
        self.assertListEqual(csv_name_list, self.name_list)

    def text_zip_reader(self):
        peoson_list = JosephReader.ZipReader('JosephusCircle.zip').begin_read()
        zip_name_list = [person.name for person in peoson_list]
        self.assertListEqual(zip_name_list, self.name_list)

    def text_read_file(self):
        peoson_list = JosephReader.read_file('JosephusCircle.zip')
        name_list = [person.name for person in peoson_list]
        self.assertListEqual(name_list, self.name_list)


def run_test():
    suite = unittest.TestSuite()
    suite.addTest(UnittextJoseph("text_deque_find_answer"))
    suite.addTest(UnittextJoseph("text_iter_find_answer"))
    suite.addTest(UnittextJoseph("text_txt_reader"))
    suite.addTest(UnittextJoseph("text_csv_reader"))
    suite.addTest(UnittextJoseph("text_zip_reader"))
    suite.addTest(UnittextJoseph("text_read_file"))
    with open('Unittest_result.txt', 'w') as test_file:
        runner = unittest.TextTestRunner(stream=test_file, verbosity=2)
        runner.run(suite)
