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
k = random.randint(-1, 2)

for _ in range(N):
    x = sd.random_number(5, 550)
    y = sd.random_number(650, 670)
    size = sd.random_number(10, 30)
    snowflakes.append([x, y, size])

sd.start_drawing()  # TODO Эту строку надо добавить перед циклом с рисованием (перед for, внутри while)
while True:
    for i, y in enumerate(snowflakes):
        point = sd.get_point(snowflakes[i][0], snowflakes[i][1])
        sd.snowflake(center=point, color=sd.background_color, length=snowflakes[i][2])
        snowflakes[i][1] -= 35 * k
        if snowflakes[i][1] < 20:
            break  # TODO До добавления снежинок не доходит из-за этого break
            # TODO Кроме того - с упавшей снежинкой тоже надо что-то делать
            # TODO Либо удалять её (опишу ниже это), либо не изменять координаты упавших снежинок
            snowdrift.append(snowflakes[i][0], snowflakes[i][1],snowflakes[i][2])
        snowflakes[i][0] += 5 * k
        point = sd.get_point(snowflakes[i][0], snowflakes[i][1])
        sd.snowflake(center=point, color=sd.COLOR_WHITE, length=snowflakes[i][2])
        # if i > 19:
        #     break
        # TODO Эту часть кода ниже надо писать после цикла, а не в нем (измените отступ)
        sd.finish_drawing()
        sd.sleep(0.1)
        if sd.user_want_exit():
            break
# TODO Упавшие снежинки можно либо запускать вновь в полет
# TODO Либо пойти по сложному пути и в этом цикле сохранять индексы упавших снежинок
# TODO А затем ещё одним циклом удалять снежинки из списка
# TODO Только список надо будет перевернуть (можно с помощью reversed())
# TODO Это нужно чтобы удалять снежинки с конца, а не с начала
# TODO А это, в свою очередь, нужно из-за сдвига, который образуется после удаления элемента списка
# TODO Удалив элемент под индексом 0, все последующие сдвинутся на -1 индекс
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


