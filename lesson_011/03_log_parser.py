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
        self.new_event_count = 0
        self.pre_line = None
        self.file = open('events.txt', 'r', encoding='cp1251')
        return self

    def __next__(self):
        for line in self.file:
            if 'NOK' in line:
                self.pre_line = line[1:17]
                if self.pre_line in self.lines:
                    self.event_count += 1
                else:
                    self.lines.append(self.pre_line)
                    self.new_event_count = self.event_count
                    self.event_count = 1
                    if len(self.lines) >= 2:
                        return self.lines[-2], self.new_event_count
        # if self.lines[-1] != 1:
        #     self.lines[-1] != self.lines[-1]
        #     return self.lines[-1], self.new_event_count
        else:
            # return self.lines[-1], self.new_event_count
            # print(f'[{self.lines[-1]}]', self.new_event_count)
            raise StopIteration()

        # Попробуйте использовать ключ-переключатель
        # не нашла информации в интернете
        # про ключ-переключатель, не пойму как можно переключить с True на False
        # TODO Это простая переменная которая равна одному значению (например True) но после срабатывания какого-либо
        # TODO условия значение изменяется (например на False)
        # TODO И другие проверки с этой переменной уже не проходят
        # TODO Т.е. надо
        # TODO 1) Создать атрибут со значением True
        # TODO 2) Создать проверку перед raise StopIteration, которая будет проверять этот атрибут с True
        # TODO 3) Если он равен True - то мы выполняем возвращение строки и счётчика и переключаем True на False
        # TODO (просто заменяем self.x = False)
        # TODO 4) Если он равен False - вызываем stopiteration
        # Первый раз, когда пайтон дойдет до сюда - он зайдет в if, переключит ключ с True на False
        # И затем выполнит return
        # В следующий раз он уже не зайдет в if, а зайдет в else и выполнит raise

grouped_events = Read()
for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')
