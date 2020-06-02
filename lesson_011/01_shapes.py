# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n):
    def draw_figure(point, start_angle, length):
        for angle in range(0, 360 - 360//n, 360//n):
            v = sd.get_vector(start_point=point, angle=angle + start_angle, length=length, width=3)
            v.draw()
            point = v.end_point
        sd.line(start_point=point, end_point=point_0, width=3)
    return draw_figure


point_0 = sd.get_point(150, 130)
draw_triangle = get_polygon(n=3)
draw_triangle(point=sd.get_point(150, 130), start_angle=13, length=100)

point_0 = sd.get_point(400, 130)
draw_square = get_polygon(n=4)
draw_square(point=sd.get_point(400, 130), start_angle=13, length=100)

point_0 = sd.get_point(150, 350)
draw_pentagon = get_polygon(n=5)
draw_pentagon(point=sd.get_point(150, 350), start_angle=13, length=100)

point_0 = sd.get_point(450, 350)
draw_hexagon = get_polygon(n=6)
draw_hexagon(point=sd.get_point(450, 350), start_angle=13, length=100)


sd.pause()
