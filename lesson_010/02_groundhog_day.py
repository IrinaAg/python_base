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
# TODO Не забывайте стиль поправлять - Code/Reformat Code
list = ['IamGodError', 'DrunkError', 'CarCrashError', 'GluttonyError','DepressionError','SuicideError']
# TODO list не стоит использовать, это название занято стандартной функцией list()
# TODO В списке надо указать исключения, а не строки. А исключения нужно ещё и создать)

def one_day():  # TODO Функция должна только возвращать карму или raise-ить исключение
    # TODO А уже функцию надо обернуть в цикл
    # Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
    # кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
    logging.basicConfig(filename="log.txt", level=logging.INFO)
    karma_level = 0
    while karma_level <= ENLIGHTENMENT_CARMA_LEVEL:
        dice = randint(1, 13)
        if dice == 1:
            exceptions = choice(list)
            # TODO Тут должен будет быть raise exceptions со случайным исключением из списка
            try:
                if exceptions[0] == int:
                    return exceptions[0]
            except:
                exceptions[0]
            logging.error(str(exceptions))
            print(exceptions)

        else:
            # TODO А тут return кармы
            karma = randint(1, 7)
            karma_level += karma
            print(karma_level)


one_day()


# https://goo.gl/JnsDqu
