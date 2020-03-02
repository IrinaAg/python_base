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
        snowflake += 1
        sd.start_drawing()
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
        print(snowflakes)
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


