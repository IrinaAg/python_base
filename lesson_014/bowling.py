# -*- coding: utf-8 -*-

# Проблема с глобальной переменной
# Она нигде не обновляется, вот все значения и копятся
# Я бы советовал вообще уйти от использования глобальной переменной
# Функция должна получать строку и независимо возвращать результат только по этой строке


def get_score(result):
    analized_res = {}
    frames = 0
    for _ in result:
        if 'X' in result[-2]:
            if result[-1].isdigit():
                raise Exception('Введено неправильное значение после strike')
        for i, k in enumerate(zip(result.replace('X', 'X-')[0::2], result.replace('X', 'X-')[1::2]), start=1):
            analized_res[i] = k
    for k, v in analized_res.items():
        frames += 1
        check_errors(v)
        counter = Counter()
        print(counter.func(v))
    print(result, '–')
    if frames != 10:
        raise Exception('Не правильное количество фреймов!')


class Counter:

    def __init__(self):
        self.total = 0

    # def game_result(): #TODO Попробовала уйти от глобальной переменной через замыкания, но не суммируется весь total
    #     total = 0 #TODO не могу понять почему, через класс так же не суммируется

    def func(self, v):
        # nonlocal total
        if 'X' in v[0]:
            self.total += 20
        elif '/' in v:
            self.total += 15
        elif '-' in v:
            if '-' in v[1]:
                self.total += 0
            else:
                self.total += int(v[1])
            if '-' in v[0]:
                self.total += 0
            else:
                self.total += int(v[0])
        else:
            if v[0].isdigit and v[1].isdigit:
                self.total += int(v[0]) + int(v[1])
        # print(total)
        return self.total
    # return func


def check_errors(v):
    if '0' in v:
        raise ValueError('Введено неправильное значение - 0')
    elif '/' in v[0]:
        raise ValueError('Spare на первом броске')
    elif 'X' in v[1]:
        raise ValueError('Strike на втором броске')
    if v[0].isdigit() and v[1].isdigit() and int(v[0]) + int(v[1]) >= 10:
        raise ValueError('Сумма одного фрейма больше 9 очков')


if __name__ == '__main__':
    # get_score('1582X332/3/62--62X')#error
    # get_score('3532X333/2/62--62X1')#error
    get_score('-532X332/3/62--62X')#102
    # get_score('3532X-33/2/62--62X1')#error
    # get_score('XXXXXXXXXX')#200
    # get_score('234--144XX23--4/X')#98

