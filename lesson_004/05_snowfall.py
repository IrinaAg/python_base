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
snowdrift = []
k = random.randint(2, 3)

for _ in range(20):
    x = sd.random_number(5, 550)
    y = sd.random_number(650, 670)
    size = sd.random_number(10, 30)
    snowflakes.append([x, y, size])
print(snowflakes)

snowflake = 0

while True:
    for x, y, size in snowflakes:
        # TODO Лучшей практикой будет for i, y in enumerate(список):
        # TODO Так у вас будет доступ и к индексам (i) и к объектам списка
        # TODO Индексы нужны потому, что при обращении к x, y, size вы изменяете только эти переменные
        # TODO а значения в списке остаются неизменными.
        # TODO Чтобы изменить координату в списке придётся обращаться к ней по индексу снежинки[индекс] -= 35 например
        snowflake += 1
        sd.start_drawing()  # TODO Эту строку надо написать до цикла, вызывать её многократно не стоит
        # TODO Это как бы метка "отсюда", указывающаяя откуда надо начать рисовать и до finish...
        point = sd.get_point(x, y)
        print(point)
        sd.snowflake(center=point, color=sd.background_color, length=size)
        y -= 35 * k
        # if y < 20:
        #     break
        x += 5
        point = sd.get_point(x, y)
        print(point)
        sd.snowflake(center=point, color=sd.COLOR_WHITE, length=size)
        snowflakes.append([x, y, size])
        # TODO Хм, интересное решение) впервые вижу такой ход
        # TODO Вам тогда по идее и for не нужен.
        # TODO Однако затратный он по ресурсам очень. Ведь список расшиярется и делает это бесконечно.
        # TODO Давайте попробуем использовать только 20 координат, добавленных до начала
        print(snowflakes)

        # TODO Эту вспомогательную часть надо писать после цикла
        sd.finish_drawing()
        sd.sleep(0.1)
        if sd.user_want_exit():
            break

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


