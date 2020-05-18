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

ENLIGHTENMENT_CARMA_LEVEL = 777
list = ['IamGodError', 'DrunkError', 'CarCrashError', 'GluttonyError','DepressionError','SuicideError']


def one_day():
    logging.basicConfig(filename="log.txt", level=logging.INFO)
    karma_level = 0
    while karma_level <= ENLIGHTENMENT_CARMA_LEVEL:
        dice = randint(1, 13)
        if dice == 1:
            exceptions = choice(list)
            try:
                if exceptions[0] == int:
                    return exceptions[0]
            except:
                exceptions[0]
            logging.error(str(exceptions))
            print(exceptions)

        else:
            karma = randint(1, 7)
            karma_level += karma
            print(karma_level)


one_day()


# https://goo.gl/JnsDqu
