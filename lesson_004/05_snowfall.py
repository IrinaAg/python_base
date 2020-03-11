# -*- coding: utf-8 -*-

import simple_draw as sd
import random

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

snowflakes = []
drift = []
# k = random.randint(-1, 2)

for _ in range(N):
    x = sd.random_number(5, 550)
    y = sd.random_number(620, 650)
    size = sd.random_number(10, 30)
    snowflakes.append([x, y, size])
    print(snowflakes)

while True:
    sd.start_drawing()
    for i, snowflake in enumerate(snowflakes):
        print(i, snowflake[1])
        point = sd.get_point(snowflake[0], snowflake[1])
        sd.snowflake(center=point, color=sd.background_color, length=snowflake[2])
        snowflake[1] -= 35
        snowflake[0] += 5
        point = sd.get_point(snowflake[0], snowflake[1])
        sd.snowflake(center=point, color=sd.COLOR_WHITE, length=snowflake[2])
        if snowflake[1] <= 15:
            drift.append(i)  # список индексов упавших снежинок, индекс доходит до 19 и опять начинает добавляться c 0
            # print(drift) #  не могу понять почему так происходить
            # если убираю отступ снежинки падают все сразу на один шаг, не поочереди
            # TODO Нужно добавить два действия
            # TODO 1) Перед циклом обновлять список упавших снежинок
            # TODO 2) Ниже удалять снежинки, используя индексы из drift
            # TODO фор индекс ин дрифт
            # TODO     снежинки.поп(индекс)
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break
    drift.reverse()
    print(drift)
    for index in list(drift):  # TODO Кстати list тут не нужен, дрифт уже является списком
        drift.pop(-1)
        # print(index)

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLORw_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg
