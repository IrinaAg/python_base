# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котoрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>  # Итератор или генератор? выбирайте что вам более понятно
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#`
# [2018-05-17 01:57] 1234


class Read:

    def __init__(self):
        self.lines = []
        self.event_count = 0

    def __iter__(self):
        self.event_count = 0
        self.file = open('events.txt', 'r', encoding='cp1251')
        return self

    def __next__(self):
        for line in self.file:
            if 'NOK' in line:
                pre_line = line
                if pre_line[1:17] in line[1:17]:
                    print(pre_line[1:17])
                    yield line
                    self.event_count += 1
                    print(self.event_count)#TODO Не понимаю в какую сторону идти(
                else:
                    self.event_count = 1


grouped_events = Read()
for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')