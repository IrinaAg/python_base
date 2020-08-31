# -*- coding: utf-8 -*-


def get_score(result):
    total = 0
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
        if 'X' in v[0]:
            total += 20
        elif '/' in v:
            total += 15
        elif '-' in v:
            if '-' in v[1]:
                total += 0
            else:
                total += int(v[1])
            if '-' in v[0]:
                total += 0
            else:
                total += int(v[0])
        else:
            if v[0].isdigit and v[1].isdigit:
                total += (int(v[0]) + int(v[1]))
    lst_result = []
    lst_result.append(result)
    lst_result.append(total)
    print(lst_result[0], '–', lst_result[1])
    if frames != 10:
        raise Exception('Не правильное количество фреймов!')
    return total


def game_result(v):
    if 'X' in v[0]:
        return + 20
    elif '/' in v:
        return + 15
    elif '-' in v:
        if '-' in v[1]:
            return 0
        else:
            int(v[1])
        if '-' in v[0]:
            return 0
        else:
            int(v[0])
    else:
        if v[0].isdigit and v[1].isdigit:
            return int(v[0]) + int(v[1])


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
    get_score(result='-532X332/3/62--62X')  # 102
    # get_score('3532X-33/2/62--62X1')#error
    # get_score('XXXXXXXXXX')#200
    # get_score('234--144XX23--4/X')#98
