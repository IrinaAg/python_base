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
        # if self.pre_line is not None:  # с синглтонами лучше использовать is вместо == или !=
        #     # Только кажется это условие вообще не нужно в текущем варианте алгоритма
        #     self.event_count = 1
        for line in self.file:
            # print(line, self.event_count)  # Иначе не учитывается первый NOK
            if 'NOK' in line:
                self.pre_line = line[1:17]
                # print(self.pre_line, self.event_count)
                if self.pre_line in self.lines:
                    # print(self.pre_line, self.event_count)
                    self.event_count += 1
                else:
                    self.lines.append(self.pre_line)
                    self.event_count = 1
                    # А тут можно возвращать не pre_line с текущей строкой
                    # А элемент из списка, который предпоследний self.lines[-2]
                    # Но для этого надо проверить, чтобы длина списка была равна 2+
                    # если возвращать self.lines[-2], то считает со сдвигом. Но так все равно выводит каждую строчку
                    # TODO Странно. Сюда алгоритм заходит, когда находит новую строку (с новой минутой)
                    # TODO Т.е. например мы считаем 38(она уже в self.lines), находим 39(добавляем её в self.lines)
                    # TODO Значит self.lines[-1] - это 39ая минута
                    # TODO А self.lines[-2] - должна быть 38ая минутая
                    # TODO т.е. когда мы находим 39ую - мы возвращаем 38ую
                    # TODO При этом возвращать элемент нужно тут.
                    # TODO И проблема осталась с event_count, нужна возможно доп переменная, чтобы в ней было
                    # TODO записано текущее число self.event_count, когда это число будет скинуто до 1
                    # TODO Тогда можно будет вернуть self.lines[-2] и count из этой переменной
                if len(self.lines) >= 1:
                    return self.lines[-1], self.event_count
        else:
            raise StopIteration()
        # return self.pre_line, self.event_count


grouped_events = Read()
for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')
    # break