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
# `
# [2018-05-17 01:57] 1234


class Read:

    def __init__(self):
        self.event_count = 0
        self.lines = []

    def __iter__(self):
        self.event_count = 0
        self.pre_line = None
        self.file = open('events.txt', 'r', encoding='cp1251')
        return self

    def __next__(self):
        # if self.pre_line != None:
        #     self.event_count = 1
        for line in self.file:
            if 'NOK' in line:
                self.pre_line = line[1:17]
                if self.pre_line in self.lines:
                    self.event_count += 1
                else:
                    self.event_count = 1
                    self.lines.append(self.pre_line)
                    print(self.pre_line)  # TODO Нужно возвращать данные через return
                    # TODO Вот так return self.pre_line, self.event_count
                # return self.pre_line, self.event_count  # Тут вывод не подойдет
                # Надо распечатывать одну строку только один раз
                print(self.event_count)
        # Последний же элемент надо отдельно вернуть тут
        return self.pre_line  # TODO Тут тоже нужна будет вторая переменная, а то вылезает ошибка
    # TODO ValueError: too many values to unpack (expected 2)


grouped_events = Read()
for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')
