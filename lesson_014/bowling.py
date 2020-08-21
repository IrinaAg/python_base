# -*- coding: utf-8 -*-

total = 0


def get_score(result, analized_res):
    # Первым делом, если есть такая возможность - от глобальных операторов надо избавляться
    # Передавайте данные через параметры - это надежнее!
    # global total
    # analized_res = {}
    # total = 0
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
        game_result(v)
    print(result, '–', total)
    if frames != 10:
        raise Exception('Не правильное количество фреймов!')
    return total


def game_result(v):
    global total
    if 'X' in v[0]:
        total += 20
    elif '/' in v:
        total += 15
    elif '-' in v[0]:
        if '-' in v[1]:
            total += 0
        elif '/' in v[1]:
            pass
        else:
            total += int(v[1])
    elif '-' in v[1]:
        if '-' in v[0]:
            total += 0
        elif 'X' in v[0]:
            pass
        else:
            total += int(v[0])
    else:
        if v[0].isdigit and v[1].isdigit:
            total += int(v[0]) + int(v[1])
    # return v


def check_errors(v):
    if '0' in v:
        raise ValueError('Введено неправильное значение - 0')
    elif '/' in v[0]:
        raise ValueError('Spare на первом броске')
    elif 'X' in v[1]:
        raise ValueError('Strike на втором броске')
    if v[0].isdigit() and v[1].isdigit() and int(v[0]) + int(v[1]) >= 10:
        print(v[0].isdigit(), v[1].isdigit(), int(v[0]), int(v[1]))
        raise ValueError('Введено неправильное значение, сумма одного фрейма больше 9 очков')


if __name__ == '__main__':
    # get_score('1582X332/3/62--62X', analized_res={})
    get_score('3532X333/2/62--62X1', analized_res = {})
    # get_score('-532X332/3/62--62X', analized_res = {})
