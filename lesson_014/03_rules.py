# -*- coding: utf-8 -*-

# Прибежал менеджер и сказал что нужно срочно изменить правила подсчета очков в игре.
# "Выходим на внешний рынок, а там правила игры другие!" - сказал он.
#
# Правила подсчета очков изменяются так:
#
# Если во фрейме страйк, сумма очков за этот фрейм будет равна количеству сбитых кеглей в этом фрейме (10 кеглей)
# плюс количество фактически сбитых кеглей за два следующих броска шара (в одном или двух фреймах,
# в зависимости от того, был ли страйк в следующем броске).
# Например: первый бросок шара после страйка - тоже страйк, то +10 (сбил 10 кеглей)
# и второй бросок шара - сбил 2 кегли (не страйк, не важно как закончится этот фрейм - считаем кегли) - то еще +2.
#
# Если во фрейме сбит спэр, то сумма очков будет равна количеству сбитых кеглей в этом фрейме (10 кеглей)
# плюс количество фактически сбитых кеглей за первый бросок шара в следующем фрейме.
#
# Если фрейм остался открытым, то сумма очков будет равна количеству сбитых кеглей в этом фрейме.
#
# Страйк и спэр в последнем фрейме - по 10 очков.
#
# То есть для игры «Х4/34» сумма очков равна 10+10 + 10+3 + 3+4 = 40,
# а для игры «ХXX347/21» - 10+20 + 10+13 + 10+7 + 3+4 + 10+2 + 3 = 92

# Необходимые изменения сделать во всех модулях. Тесты - дополнить.

# "И да, старые правила должны остаться! для внутреннего рынка..." - уточнил менеджер напоследок.


def get_score_woldwide(result):
    total = 0
    analized_res = {}
    frames = 0
    for _ in result:
        if 'X' in result[-2]:
            if result[-1].isdigit():
                raise Exception('Введено неправильное значение после strike')
        for i, k in enumerate(zip(result.replace('X', 'X-')[0::2], result.replace('X', 'X-')[1::2]), start=1):
            # print(i, k)
            analized_res[i] = k
            # print(i)
    for k, v in analized_res.items():
        print(k, v)
        frames += 1
        check_errors(v)
        if 'X' in v:
            if 'X' in analized_res[k + 1]:
                if 'X' in analized_res[k + 2]:
                    total += 30
                    print(total, 'x')
                elif '-' in analized_res[k + 2][0]:
                    total += 20
                    print(total, 'x1')
                else:
                    total += 20 + int(analized_res[k + 2][0])
                    print(total, 'x2')
            elif '/' in analized_res[k + 1]:
                total += 20
                # print(total)
            elif '-' in analized_res[k + 1][0]:
                if '-' in analized_res[k + 1][1]:
                    total += 10
                    # print(total)
                else:
                    total += 10 + int(analized_res[k + 1][1])
                    # print(total)
            elif '-' in analized_res[k + 1][1]:
                total += 10 + int(analized_res[k + 1][0])
                # print(total, '-')
            else:
                total += 10 + int(analized_res[k + 1][0]) + int(analized_res[k + 1][1])
                # print(total, '-')
        elif '/' in v:
            if 'X' in analized_res[k + 1]:
                total += 20
                # print(total)
            elif '/' in analized_res[k + 1][0]:
                raise ValueError('Spare на первом броске')
            elif '-' in analized_res[k + 1][0]:
                total += 10
                # print(total, '-')
            else:
                total += 10 + int(analized_res[k + 1][0])
                # print(total)
        elif '-' in v[0]:
            if '-' in v[1]:
                total += 0
            elif '/' in v[1]:
                pass
            else:
                total += int(v[1])
                # print(total, '-')
        elif '-' in v[1]:
            if '-' in v[0]:
                total += 0
            elif 'X' in v[0]:
                pass
            else:
                total += int(v[0])
                # print(total, '-')
        else:
            if v[0].isdigit and v[1].isdigit:
                total += int(v[0]) + int(v[1])
                # print(total, '-')
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
    #TODO Перебором получается портянка, но по другому не понимаю как это реализовать можете какие-то примеры показать?
    if 'X' in v:
        if 'X' in analized_res[k + 1]:
            if 'X' in analized_res[k + 2]:
                print(analized_res[k])
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
    get_score_woldwide('XXX347/21--------')#92
    # print('Х4/34XXXXXXX'.replace('X', 'X-'))  # Причина в том, что первый X был на одном языке а остальные на другом
    # Можно сделать два replace, одним заменить русские символы на англ, вторым уже заменять на X-
    # print('X4/34XXXXXXX'.replace('X', 'X-'))
    # get_score_woldwide('X4/34--------------')#40
    # get_score_woldwide('X4/34----------X--')#50
