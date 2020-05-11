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

    def start_method(self):
        self.unzip()
        self.open()
        # TODO Идея в том, чтобы метод сортировки был один
        self.sort_requency_descending()
        self.sort_frequency_ascending()
        self.sort_alphabetically_ascending()
        self.sort_alphabetically_descending()
        self.print_data()

    def sort_requency_descending(self):
        pass

    def sort_frequency_ascending(self):
        pass

    def sort_alphabetically_ascending(self):
        pass

    def sort_alphabetically_descending(self):
        pass

    def print_data(self):
        pass

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
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


class Sorted(Statistics):  # TODO И в каждом дочернем классе метод сортировки должен быть переопределен по-своему

    def __init__(self):
        super().__init__()
        self.sort_data = []

    def sort_requency_descending(self):
        for sort_data in sorted(self.stat.items(), key=lambda para: (para[1], para[0]), reverse=True):
            self.sort_data.append(sort_data)

    def sort_frequency_ascending(self):
        for sort_data in sorted(self.stat.items(), key=lambda para: (para[1], para[0]), reverse=False):
            self.sort_data.append(sort_data)

    def sort_alphabetically_ascending(self):
        for sort_data in sorted(self.stat.items(), key=lambda para: (para[0], para[1]), reverse=True):
            self.sort_data.append(sort_data)

    def sort_alphabetically_descending(self):
        for sort_data in sorted(self.stat.items(), key=lambda para: (para[0], para[1]), reverse=False):
            self.sort_data.append(sort_data)


class Print_data(Sorted):  # TODO имя не соответствует правилам CamelCase

    def print_data(self):  # TODO Сам метод с принтами можно оставить в родительском классе
        # TODO я имел ввиду в прошлый раз, что он должен заниматься только распечатыванием данных, без сортировки
        print('+' + '-' * 10 + '+' + '-' * 10 + '+')
        print('|{name:^10}|'.format(name='буква'), '{key:^9}|'.format(key='частота'))
        print('+' + '-' * 10 + '+' + '-' * 10 + '+')
        for sort_data in self.sort_data:
            print('|{name:^10}|'.format(name=sort_data[0]), '{key:^9}|'.format(key=sort_data[1]))
            print('+' + '-' * 10 + '+' + '-' * 10 + '+')
        print('|{name:^10}|'.format(name='итого'), '{key:^9}|'.format(key=self.count))
        print('+' + '-' * 10 + '+' + '-' * 10 + '+')


statis = Statistics(file_name='voyna-i-mir.txt.zip')
statis1 = Sorted()
statis2 = Print_data()
statis2.start_method()

# class Statistics:
#
#     def __init__(self, file_name):
#         self.file_name = file_name
#         self.stat = {}
#         self.count = 0
#
#     def unzip(self):
#         zfile = zipfile.ZipFile(self.file_name, 'r')
#         for filename in zfile.namelist():
#             zfile.extract(filename)
#
#     def open(self, file_name):
#         # stat = {}
#         # k = 0
#         with open(file_name, 'r', encoding='cp1251') as file:
#             for line in file:
#                 for char in line:
#                     if char.isalpha():
#                         self.count += 1
#                         if char in self.stat:
#                             self.stat[char] += 1
#                         else:
#                             self.stat[char] = 1
#             # print(stat)
#             # print(k)
#
#     def sort(self):
#         print('+' + '-' * 10 + '+' + '-' * 10 + '+')
#         print('|{name:^10}|'.format(name='буква'), '{key:^9}|'.format(key='частота'))
#         # for i in sorted(stat.items(), key=lambda para: (para[1], para[0]), reverse=True):
#         # for i in sorted(stat.items(), key=lambda para: (para[1], para[0]), reverse=False):
#         # for i in sorted(stat.items(), key=lambda para: (para[0], para[1]), reverse=True):
#         for i in sorted(self.stat.items(), key=lambda para: (para[0], para[1]), reverse=False):
#             print('+' + '-' * 10 + '+' + '-' * 10 + '+')
#             print('|{name:^10}|'.format(name=i[0]), '{key:^9}|'.format(key=i[1]))
#         print('+' + '-' * 10 + '+' + '-' * 10 + '+')
#         print('|{name:^10}|'.format(name='итого'), '{key:^9}|'.format(key=self.count))
#         print('+' + '-' * 10 + '+' + '-' * 10 + '+')
#
#
# statis = Statistics(file_name='voyna-i-mir.txt.zip')
# statis.unzip()
# statis.open(file_name='voyna-i-mir.txt')
# statis.sort()

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://goo.gl/Vz4828
#   и пример https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4
