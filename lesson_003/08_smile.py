# -*- coding: utf-8 -*-

# (определение функций)
import random
import simple_draw as sd

# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: координата X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.


radius = 60
eye = radius // 8
coordinate_x, coordinate_y = 300, 300
color = sd.COLOR_GREEN


def smile(coordinate_x, coordinate_y, color):
    eye_left = sd.get_point(point.x - 25, point.y + 20)
    eye_right = sd.get_point(point.x + 25, point.y + 20)
    start_point = sd.get_point(point.x - 45, point.y - 10)
    end_point = sd.get_point(point.x - 25, point.y - 30)
    start_point1 = sd.get_point(point.x - 25, point.y - 30)
    end_point1 = sd.get_point(point.x + 20, point.y - 30)
    start_point2 = sd.get_point(point.x + 20, point.y - 30)
    end_point2 = sd.get_point(point.x + 40, point.y - 10)
    sd.circle(center_position=point, radius=radius, width=1, color=color)
    sd.circle(center_position=eye_left, radius=eye, width=1, color=color)
    sd.circle(center_position=eye_right, radius=eye, width=1, color=color)
    sd.line(start_point=start_point, end_point=end_point, color=color, width=1)
    sd.line(start_point=start_point1, end_point=end_point1, color=color, width=1)
    sd.line(start_point=start_point2, end_point=end_point2, color=color, width=1)


for _ in range(10):
    point = sd.random_point()
    smile(coordinate_x, coordinate_y, color)


sd.pause()
