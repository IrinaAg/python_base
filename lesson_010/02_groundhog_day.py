# -*- coding: utf-8 -*-
from random import randint, choice
import logging

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.
ENLIGHTENMENT_KARMA_LEVEL = 777


class IamGodError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


class SuicideError(Exception):
    pass


lst = [IamGodError, DrunkError, CarCrashError, GluttonyError, DepressionError, SuicideError]

file = open('log.txt', 'a', encoding='utf8')


def one_day():
    dice = randint(1, 13)
    if dice == 13:
        exceptions = choice(lst)
        raise exceptions
    else:
        karma = randint(1, 7)
        return karma


karma_level = 0
while karma_level < ENLIGHTENMENT_KARMA_LEVEL:
    try:
        karma_level += one_day()
        # print(karma_level, file=file)
    except IamGodError as exc:
        print('Я Бог', file=file)
    except DrunkError:
        print('Напился', file=file)
    except CarCrashError:
        print('Авария', file=file)
    except GluttonyError:
        print('Обжорство', file=file)
    except DepressionError:
        print('Депрессия', file=file)
    except SuicideError:
        print('Суицид', file=file)

# https://goo.gl/JnsDqu
