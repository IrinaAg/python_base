# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg
colors = {
    '0': {'color_name': 'red', 'sd_name': sd.COLOR_RED},
    '1': {'color_name': 'orange', 'sd_name': sd.COLOR_ORANGE},
    '2': {'color_name': 'yellow', 'sd_name': sd.COLOR_YELLOW},
    '3': {'color_name': 'green', 'sd_name': sd.COLOR_GREEN},
    '4': {'color_name': 'cyan', 'sd_name': sd.COLOR_CYAN},
    '5': {'color_name': 'blue', 'sd_name': sd.COLOR_BLUE},
    '6': {'color_name': 'purple', 'sd_name': sd.COLOR_PURPLE}
}
print('Возможные цвета:', '0 : ' + colors['0']['color_name'], '1 : ' + colors['1']['color_name'],
      '2 : ' + colors['2']['color_name'], '3 : ' + colors['3']['color_name'], '4 : ' + colors['4']['color_name'],
      '5 : ' + colors['5']['color_name'], '6 : ' + colors['6']['color_name'], sep='\n')

while True:
    user_input = input('Введите желаемый цвет >')
    if user_input in colors:
        color = colors[user_input]['sd_name']
        break
    else:
        print("Вы ввели некорректный номер")


def draw_figure(point, angle, length):
    for angle in range(0, 360 - angle, angle):
        v = sd.get_vector(start_point=point, angle=angle + 25, length=length, width=3)
        v.draw(color=color)
        point = v.end_point
    sd.line(start_point=point, end_point=point_0, color=color, width=3)


def triangle(point, angle, length):
    draw_figure(point=point, angle=angle, length=length)


point_0 = sd.get_point(150, 130)
side = 3
triangle(point=point_0, angle=360 // side, length=100)


def square(point, angle=25, length=100, width=3):
    draw_figure(point=point, angle=angle, length=length)


point_0 = sd.get_point(400, 130)
side = 4
square(point=point_0, angle=360//side, length=100)


def pentagon(point, angle=25, length=100, width=3):
    draw_figure(point=point, angle=angle, length=length)


point_0 = sd.get_point(150, 350)
side = 5
pentagon(point=point_0, angle=360//side, length=100)


def hexagon(point, angle, length=100, width=3):
    draw_figure(point=point, angle=angle, length=length)


point_0 = sd.get_point(450, 350)
side = 6
hexagon(point=point_0, angle=360//side, length=100)

sd.pause()
