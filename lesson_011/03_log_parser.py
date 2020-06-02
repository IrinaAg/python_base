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
        self.event_count = 0
        self.lines = {}

    def __iter__(self):
        self.event_count = 0
        self.pre_line = None
        self.file = open('events.txt', 'r', encoding='cp1251')
        return self

    def __next__(self):
        if self.pre_line != None:
            self.event_count = 1
        for line in self.file:
            if 'NOK' in line:
                if self.pre_line == None:  # TODO Тут вы обрабатываете частный случай для первой строки
                    self.pre_line = line[1:17]
                    self.event_count += 1
                # TODO Но как пайтон поймёт, что в новой строке пришла новая минута, а не старая?
                # TODO т.е. записалась в pre_line 19:38
                # TODO в какой-то новой строке приходит 19:39
                # TODO Надо как-то сравнить переменную, в которой записана прошлая минута
                # TODO С минутой, которая пришла в новой строке
                # TODO Если минута новая - изменять переменную, обновлять счётчик
                # TODO Но при этом после этих изменений надо отправить старую минуту и старый счётчик
                # TODO Т.е. надо их где-то сохранить, изменить и отправить.
                # TODO В этом и преимущество генератора было бы, т.к. он бы после yield позволил внести изменения
                else:
                    return self.pre_line, self.event_count


grouped_events = Read()
for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')