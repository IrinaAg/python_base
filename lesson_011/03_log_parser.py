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
                if self.pre_line in self.lines:  # распечатывается каждая строчка, не могу вывести только
                    self.event_count += 1  # последнюю посчитанную
                    # self.lines[self.pre_line] += 1
                # Но как пайтон поймёт, что в новой строке пришла новая минута, а не старая?
                # т.е. записалась в pre_line 19:38
                # в какой-то новой строке приходит 19:39
                # Надо как-то сравнить переменную, в которой записана прошлая минута
                # С минутой, которая пришла в новой строке
                # Если минута новая - изменять переменную, обновлять счётчик
                # Но при этом после этих изменений надо отправить старую минуту и старый счётчик
                # Т.е. надо их где-то сохранить, изменить и отправить.
                # В этом и преимущество генератора было бы, т.к. он бы после yield позволил внести изменения
                else:
                    # self.lines[self.pre_line] = 1
                    self.event_count = 1
                self.lines.append(self.pre_line)
                return self.pre_line, self.event_count  # TODO Тут вывод не подойдет
                # TODO Надо распечатывать одну строку только один раз
                # print(self.pre_line, self.event_count)
                # print(self.lines)
        # TODO Последний же элемент надо отдельно вернуть тут


grouped_events = Read()
for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')
