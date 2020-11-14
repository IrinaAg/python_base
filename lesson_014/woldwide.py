# Наш фрейм
x = ['X-', 'X-', 'X-', '34', '4/', '21']


def add_strike_points(frames, index):
    result = 0
    throw = 0
    for _ in range(2):
        if index >= len(frames):
            break

        first_frame = frames[index + 1]
        second_frame = frames[index + 2]
        if first_frame[throw] == 'X':
            result += 10
            index += 1
        elif first_frame[throw].isdigit():
            result += int(first_frame[throw]) + int(second_frame[throw])
            throw += 1
        elif second_frame[throw] == 'X':
            result += 10
            throw += 1
        elif first_frame[throw] == '/':
            result += 10
    return result


# print(add_strike_points(x, 0))


def add_spare_points(frames, index):
    result = 0
    throw = 0
    for _ in range(2):
        if index >= len(frames):
            print(index)
            break

        first_frame = frames[index + 1]
        second_frame = frames[index + 2]
        if first_frame[throw] == '/':
            print(index)
            result += 10
        elif first_frame[throw] == '/':
            raise ValueError('Spare на первом броске')
        elif first_frame[throw] == '-':
            result += 10
        else:
            result += int(second_frame[throw])
            throw += 1
    return result


# print(add_spare_points(x, 3))
#TODO оставила старый код, не получается сделать с разбивкой отдельно на spare
#TODO и strike больше двух месяцев

def get_score_woldwide(result):
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
        if 'X' in v:
            if 'X' in analized_res[k + 1]:
                if 'X' in analized_res[k + 2]:
                    total += 30
                elif '-' in analized_res[k + 2][0]:
                    total += 20
                else:
                    total += 20 + int(analized_res[k + 2][0])
            elif '/' in analized_res[k + 1]:
                total += 20
            elif '-' in analized_res[k + 1][0]:
                if '-' in analized_res[k + 1][1]:
                    total += 10
                else:
                    total += 10 + int(analized_res[k + 1][1])
            elif '-' in analized_res[k + 1][1]:
                total += 10 + int(analized_res[k + 1][0])
            else:
                total += 10 + int(analized_res[k + 1][0]) + int(analized_res[k + 1][1])
        elif '/' in v:
            if 'X' in analized_res[k + 1]:
                total += 20
            elif '/' in analized_res[k + 1][0]:
                raise ValueError('Spare на первом броске')
            elif '-' in analized_res[k + 1][0]:
                total += 10
            else:
                total += 10 + int(analized_res[k + 1][0])
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
    lst_result = []
    lst_result.append(result)
    lst_result.append(total)
    print(lst_result[0], '–', lst_result[1])
    if frames != 10:
        raise Exception('Не правильное количество фреймов!')
    return total


def woldwide(k, v, analized_res):
    # Перебор в лоб - не самое эффективное решение
    # Я бы посоветовал подумать в сторону функции, которая возвращает очки за следующие два броска
    # Т.е. например вызов func(result='Х4/34XXXXXXX', frame_number=1) -вернёт-> 10 (4+6)
    # И отдельную функцию можно для одного броска (либо параметром указывать за сколько бросков нужны доп очки
    if 'X' in v:
        if 'X' in analized_res[k + 1]:
            if 'X' in analized_res[k + 2]:
                # print(analized_res[k])
                return + 30
            elif '-' in analized_res[k + 2][0]:
                return + 20
            else:
                return + 20 + int(analized_res[k + 2][0])
        elif '/' in analized_res[k + 1]:
            return + 20
        elif '-' in analized_res[k + 1][0]:
            if '-' in analized_res[k + 1][1]:
                return + 10
            else:
                return + 10 + int(analized_res[k + 1][1])
        elif '-' in analized_res[k + 1][1]:
            return + 10 + int(analized_res[k + 1][0])
        else:
            return + 10 + int(analized_res[k + 1][0]) + int(analized_res[k + 1][1])
    elif '/' in v:
        if 'X' in analized_res[k + 1]:
            return + 20
        elif '/' in analized_res[k + 1][0]:
            raise ValueError('Spare на первом броске')
        elif '-' in analized_res[k + 1][0]:
            return + 10
        else:
            return + 10 + int(analized_res[k + 1][0])
    elif '-' in v[0]:
        if '-' in v[1]:
            return + 0
        elif '/' in v[1]:
            pass
        else:
            return + int(v[1])
    elif '-' in v[1]:
        if '-' in v[0]:
            return + 0
        elif 'X' in v[0]:
            pass
        else:
            return + int(v[0])
    else:
        if v[0].isdigit and v[1].isdigit:
            return + int(v[0]) + int(v[1])


def check_errors(v):
    if '0' in v:
        raise ValueError('Введено неправильное значение - 0')
    elif '/' in v[0]:
        raise ValueError('Spare на первом броске')
    elif 'X' in v[1]:
        raise ValueError('Strike на втором броске')
    if v[0].isdigit() and v[1].isdigit() and int(v[0]) + int(v[1]) >= 31:
        raise ValueError('Сумма одного фрейма больше 31 очков')


if __name__ == '__main__':
    # get_score_woldwide('-532X332/3/62--62X')  # 102
    # get_score_woldwide('XXXXXXXXXX')#200
    # get_score_woldwide('234--144XX23--4/X')#98
    get_score_woldwide('XXX347/21--------')  # 92
    # print('Х4/34XXXXXXX'.replace('X', 'X-'))
    # print('X4/34XXXXXXX'.replace('X', 'X-'))
    get_score_woldwide('X4/34--------------')#40
    get_score_woldwide('X4/34----------X--')#50