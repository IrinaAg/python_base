# -*- coding: utf-8 -*-

import simple_draw as sd
import random

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длина ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

sd.resolution = (1200, 800)
point_0 = sd.get_point(600, 0)
root_point = sd.get_point(300, 30)


def draw_branch(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()
    return v1.end_point


# angle_0 = 90
# length_0 = 200
# next_point_right = draw_branch(point=point_0, angle=angle_0, length=length_0)
# next_angle = angle_0 - 30
# next_length = length_0 * .75
# next_point_right = draw_branch(point=next_point_right, angle=next_angle, length=next_length)
# next_angle = next_angle - 30
# next_length = next_length * .75
# next_point_right = draw_branch(point=next_point_right, angle=next_angle, length=next_length)
# next_point_left = draw_branch(point=point_0, angle=angle_0, length=length_0)
# next_angle_left = angle_0 + 30
# next_length = length_0 * .75
# next_point_left = draw_branch(point=next_point_left, angle=next_angle_left, length=next_length)
# next_angle_left = next_angle_left + 30
# next_length = next_length * .75
# next_point_left = draw_branch(point=next_point_left, angle=next_angle_left, length=next_length)

# angle_0 = 90
# length_0 = 200
#
# next_angle = angle_0
# next_angle_left = angle_0
# next_length = length_0
# next_length_left = length_0
# next_point_right = point_0
# next_point_left = point_0
#
# while next_length > 10:
#     next_point_right = draw_branch(point=next_point_right, angle=next_angle, length=next_length)
#     next_angle = next_angle - 30
#     next_length = next_length * .75
#     print(next_point_right)
#     print(next_angle)
#     print(next_length)
#
# while next_length_left > 10:
#     next_point_left = draw_branch(point=next_point_left, angle=next_angle_left, length=next_length_left)
#     next_angle_left = next_angle_left + 30
#     next_length_left = next_length_left * .75


# def draw_branch(point, angle, length): # функция как в примере
#     if length < 3:
#         return
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
#     v1.draw()
#     next_point = v1.end_point
#     next_angle = angle + 30
#     next_length = length * .75
#     next_angle_left = angle - 30
#     draw_branch(point=next_point, angle=next_angle, length=next_length)
#     draw_branch(point=next_point, angle=next_angle_left, length=next_length)
#
#
# draw_branch(point=point_0, angle=90, length=200)

# def draw_branch(point, angle, length):  # функция из задания
#     if length < 10:
#         return
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
#     v1.draw()
#     next_point = v1.end_point
#     next_angle = angle + 30
#     next_length = length * .75
#     next_angle_left = angle - 30
#     draw_branch(point=next_point, angle=next_angle, length=next_length)
#     draw_branch(point=next_point, angle=next_angle_left, length=next_length)
#
#
# draw_branch(point=root_point, angle=90, length=100)

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg


def draw_branch(point, angle, length): # функция как в примере
    if length < 3:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
    v1.draw()
    next_point = v1.end_point
    next_angle = angle + sd.random_number(18, 42)
    next_length = length * random.uniform(.6, .9)
    next_angle_left = angle - sd.random_number(18, 42)
    draw_branch(point=next_point, angle=next_angle, length=next_length)
    draw_branch(point=next_point, angle=next_angle_left, length=next_length)


draw_branch(point=point_0, angle=90, length=200)

# Пригодятся функции
# sd.random_number()

sd.pause()


