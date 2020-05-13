# -*- coding: utf-8 -*-
import zipfile


# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.


class Statistics:

    def __init__(self, file_name='voyna-i-mir.txt.zip'):
        self.file_name = file_name
        self.stat = {}
        self.count = 0
        self.sort_data = []

    def start_method(self):
        self.unzip()
        self.open()
        self.sort()
        self.print_data()

    def sort(self):
        pass

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        filename = None
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename

    def open(self):
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        self.count += 1
                        if char in self.stat:
                            self.stat[char] += 1
                        else:
                            self.stat[char] = 1

    def print_data(self):
        print('+' + '-' * 10 + '+' + '-' * 10 + '+')
        print('|{name:^10}|'.format(name='буква'), '{key:^9}|'.format(key='частота'))
        print('+' + '-' * 10 + '+' + '-' * 10 + '+')
        for sort_data in self.sort_data:
            print('|{name:^10}|'.format(name=sort_data[0]), '{key:^9}|'.format(key=sort_data[1]))
            print('+' + '-' * 10 + '+' + '-' * 10 + '+')
        print('|{name:^10}|'.format(name='итого'), '{key:^9}|'.format(key=self.count))
        print('+' + '-' * 10 + '+' + '-' * 10 + '+')


class Sorted(Statistics):

    def __init__(self):
        super().__init__()
        self.sort_data = []

    def sort(self):
        for sort_data in sorted(self.stat.items(), key=lambda para: (para[1], para[0]), reverse=True):
            self.sort_data.append(sort_data)


class Sorted2(Statistics):

    def __init__(self):
        super().__init__()
        self.sort_data = []

    def sort(self):
        for sort_data in sorted(self.stat.items(), key=lambda para: (para[1], para[0]), reverse=False):
            self.sort_data.append(sort_data)


class Sorted3(Statistics):

    def __init__(self):
        super().__init__()
        self.sort_data = []

    def sort(self):
        for sort_data in sorted(self.stat.items(), key=lambda para: (para[0], para[1]), reverse=True):
            self.sort_data.append(sort_data)


class Sorted4(Statistics):

    def __init__(self):
        super().__init__()
        self.sort_data = []

    def sort(self):
        for sort_data in sorted(self.stat.items(), key=lambda para: (para[0], para[1]), reverse=False):
            self.sort_data.append(sort_data)


statis = Statistics(file_name='voyna-i-mir.txt.zip')
statis1 = Sorted()
# statis1.start_method()
statis2 = Sorted2()
statis2.start_method()
statis3 = Sorted3()
# statis3.start_method()
statis4 = Sorted4()
# statis4.start_method()


# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://goo.gl/Vz4828
#   и пример https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4
#зачет!