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


while True:
    sd.start_drawing()
    for i, snowflake in enumerate(snowflakes):
        point = sd.get_point(snowflake[0], snowflake[1])
        sd.snowflake(center=point, color=sd.background_color, length=snowflake[2])
        snowflake[1] -= 35
        if snowflake[1] <= 25:
            drift.append(i)

            # TODO Разворот списка и цикл по drift надо вынести из цикла по снежинкам
            # TODO Если удалять элементы списка, по которому идёт цикл (вы удаляете из snowflakes внутри цикла по нему)
            # TODO То будут происходить пропуски элементов
            drift.reverse()
        for index in drift:
            snowflakes.pop(-1)
            if len(snowflakes) == 0:
                break
        snowflake[0] += 5
        point = sd.get_point(snowflake[0], snowflake[1])
        sd.snowflake(center=point, color=sd.COLOR_WHITE, length=snowflake[2])
    # TODO Структура примерно такая должна получится(внимание на отступы)
    # while
    #     for по снежинкам
    #         закрашивание -- сдвиг(+добавление индексов упавших снежинок) -- рисование
    #     for по индексам
    #         удаление снежинок из списка
    #     обновление списка с индексами -- TODO Важный этап, иначе индексы будут накапливаться с каждой итерацией

    # TODO Обратите внимание, что удалять надо по индексам, а не (-1), как тут snowflakes.pop(-1)
    # TODO переменная цикла по-очереди перебирает индексы упавших снежинок, вы эту переменную подставляете
    # TODO в метод удаления снежинок

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
