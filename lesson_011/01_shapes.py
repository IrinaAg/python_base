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


def get_polygon(n):  # TODO 'n' должно быть использовано в фигуре ниже, вместо angle
    def draw_figure(point, angle, start_angle, length):
        # TODO Можно вот здесь например этот angle вычислить как 360//n
        for angle in range(0, 360 - angle, angle):  # TODO Только используйте разные имена для
            # TODO переменной в цилк и переменной в параметрах.
            v = sd.get_vector(start_point=point, angle=angle + start_angle, length=length, width=3)
            v.draw()
            point = v.end_point
        sd.line(start_point=point, end_point=point_0, width=3)
    return draw_figure


point_0 = sd.get_point(150, 130)
draw_triangle = get_polygon(n=3)
draw_triangle(point=sd.get_point(150, 130), angle=120, start_angle=13, length=100)

point_0 = sd.get_point(400, 130)
draw_square = get_polygon(n=4)
draw_square(point=sd.get_point(400, 130), angle=90, start_angle=13, length=100)

point_0 = sd.get_point(150, 350)
draw_pentagon = get_polygon(n=5)
draw_pentagon(point=sd.get_point(150, 350), angle=72, start_angle=13, length=100)

point_0 = sd.get_point(450, 350)
draw_hexagon = get_polygon(n=6)
draw_hexagon(point=sd.get_point(450, 350), angle=60, start_angle=13, length=100)


sd.pause()
