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
k = random.randint(-1, 2)

for _ in range(N):
    x = sd.random_number(5, 550)
    y = sd.random_number(620, 650)
    size = sd.random_number(10, 30)
    snowflakes.append([x, y, size])

while True:
    sd.start_drawing()
    for i, y in enumerate(snowflakes):
        point = sd.get_point(snowflakes[i][0], snowflakes[i][1])
        sd.snowflake(center=point, color=sd.background_color, length=snowflakes[i][2])
        snowflakes[i][1] -= 35 * k
        snowflakes[i][0] += 5 * k
        point = sd.get_point(snowflakes[i][0], snowflakes[i][1])
        sd.snowflake(center=point, color=sd.COLOR_WHITE, length=snowflakes[i][2])
        if snowflakes[i][1] < 20:
            snowflakes.append(i)
            snowflakes.reverse()
            for index in range(N):
                snowflakes.pop()
                # print(snowflakes)
        # TODO Эту часть кода ниже надо писать после цикла, а не в нем (измените отступ)
        # TODO если убираю отступ снежинки падают все сразу, не поочереди
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
