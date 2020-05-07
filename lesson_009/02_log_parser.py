# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.


class Read:

    def __init__(self, file_name):
        self.file_name = file_name
        self.lines = {}

    def start_method(self):
        self.minute()
        self.hour()
        self.month()
        self.year()
        self.record()

    def minute(self):
        pass

    def hour(self):
        pass

    def month(self):
        pass

    def year(self):
        pass

    def record(self):
        file = open('out.txt', 'w', encoding='utf8')
        for i in sorted(self.lines.items()):
            print('[' + i[0] + ']' '-', i[1], file=file)
        file.close()


# TODO Тут можно вместо числа 17, 14 и тд использовать атрибут класса.
# TODO И в каждом наследнике изменять этот атрибут на нужный.
class Minute(Read):

    def minute(self, file_name='events.txt'):
        with open(file_name, 'r', encoding='cp1251') as file:
            for line in file:
                if 'NOK' in line:
                    char = line[1:17]
                    if char in self.lines:
                        self.lines[char] += 1
                    else:
                        self.lines[char] = 1


class Hour(Read):

    def hour(self, file_name='events.txt'):
        with open(file_name, 'r', encoding='cp1251') as file:
            for line in file:
                if 'NOK' in line:
                    char = line[1:14]
                    if char in self.lines:
                        self.lines[char] += 1
                    else:
                        self.lines[char] = 1


class Month(Read):

    def month(self, file_name='events.txt'):
        with open(file_name, 'r', encoding='cp1251') as file:
            for line in file:
                if 'NOK' in line:
                    char = line[1:8]
                    if char in self.lines:
                        self.lines[char] += 1
                    else:
                        self.lines[char] = 1


class Year(Read):

    def year(self, file_name='events.txt'):
        with open(file_name, 'r', encoding='cp1251') as file:
            for line in file:
                if 'NOK' in line:
                    char = line[1:5]
                    if char in self.lines:
                        self.lines[char] += 1
                    else:
                        self.lines[char] = 1


read_file = Read(file_name='events.txt')
read_file1 = Minute(Read)
read_file1.start_method()


# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
# read_file2 = Hour(Read)
# read_file2.start_method()

#  - по месяцу
# read_file3 = Month(Read)
# read_file3.start_method()

#  - по году
# read_file4 = Year(Read)
# read_file4.start_method()

# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
