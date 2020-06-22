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
        if self.pre_line != None:  # TODO с синглтонами лучше использовать is вместо == или !=
            # TODO Только кажется это условие вообще не нужно в текущем варианте алгоритма
            self.event_count = 1
        for line in self.file:
            print(line, self.event_count)  # TODO Иначе не учитывается первый NOK
            if 'NOK' in line:
                self.pre_line = line[1:17]
                if self.pre_line in self.lines:
                    self.event_count += 1
                    #self.lines.append(self.pre_line)  # TODO Эта строка как мне кажется не нужна
                else:
                    self.lines.append(self.pre_line)
                    # TODO А тут можно возвращать не pre_line с текущей строкой
                    # TODO А элемент из списка, который предпоследний self.lines[-2]
                    # TODO Но для этого надо проверить, чтобы длина списка была равна 2+
                    return self.pre_line, self.event_count
                    # счетчик считает, но выводится в сделующей строчке
        else:
            raise StopIteration()
        # return self.pre_l ine, self.event_count


grouped_events = Read()
for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')
    break