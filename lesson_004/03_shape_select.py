# -*- coding: utf-8 -*-

import simple_draw as sd


# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg


def draw_figure(point, angle, start_angle, length):
    for angle in range(0, 360 - angle, angle):
        v = sd.get_vector(start_point=point, angle=angle + start_angle, length=length, width=3)
        v.draw()
        point = v.end_point
    sd.line(start_point=point, end_point=point_0, width=3)


def triangle(point, start_angle, length):
    draw_figure(point=point, angle=120, start_angle=start_angle, length=length)


def square(point, start_angle, length):
    draw_figure(point=point, angle=90, start_angle= start_angle, length=length)


def pentagon(point, start_angle, length):
    draw_figure(point=point, angle=72, start_angle=start_angle, length=length)


def hexagon(point, start_angle, length):
    draw_figure(point=point, angle=60, start_angle=start_angle, length=length)


point_0 = sd.get_point(300, 250)


functions = {
    '0': {'func_name': 'треугольник', 'func': triangle},
    '1': {'func_name': 'квадрат', 'func': square},
    '2': {'func_name': 'пятиугольник', 'func': pentagon},
    '3': {'func_name': 'шестиугольник', 'func': hexagon}
}
print('Возможные фигуры:')
for code, val in functions.items():
    print(code, ':', val['func_name'])

while True:
    user_input = input('Введите желаемую фигуру >')
    if user_input in functions:
        function = functions[user_input]['func']
        function(point=point_0, start_angle=25, length=100)
        break
    else:
        print("Вы ввели некорректный номер")

sd.pause()
