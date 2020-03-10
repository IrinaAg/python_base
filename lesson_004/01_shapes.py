# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg


def draw_figure(point, angle, start_angle, length):
    for angle in range(0, 360 - angle, angle):
        v = sd.get_vector(start_point=point, angle=angle + start_angle, length=length, width=3)
        v.draw()
        point = v.end_point
    sd.line(start_point=point, end_point=point_0, width=3)


def triangle(point, angle, start_angle, length):
    draw_figure(point=point, angle=angle, start_angle=start_angle, length=length)


def square(point, angle, start_angle, length):
    draw_figure(point=point, angle=angle, start_angle=start_angle, length=length)


def pentagon(point, angle, start_angle, length):
    draw_figure(point=point, angle=angle, start_angle=start_angle, length=length)


def hexagon(point, angle, start_angle, length):
    draw_figure(point=point, angle=angle, start_angle=start_angle, length=length)


point_0 = sd.get_point(150, 130)
triangle(point=point_0, angle=120, start_angle=25, length=100)

point_0 = sd.get_point(400, 130)
square(point=point_0, angle=90, start_angle=25, length=100)

point_0 = sd.get_point(150, 350)
pentagon(point=point_0, angle=72, start_angle=25, length=100)

point_0 = sd.get_point(450, 350)
hexagon(point=point_0, angle=60, start_angle=25, length=100)

sd.pause()

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44? Код писать не нужно, просто представь объем работы... и запомни это.

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
