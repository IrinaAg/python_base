# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg
print('Возможные фигуры:', '0 : треугольник', '1 : квадрат', '2 : пятиугольник', '3 : шестиугольник', sep='\n')
# TODO Нам надо реализовать выбор функции пользователем
# TODO Для этого мы выбираем тот же путь, что в 02 с выбором цвета.
# TODO Берем ту же структуру данных. Чтобы хранить функции в словаре - надо указать их без скобок, только имя
# TODO Запустить её можно будет следующим образом:
# TODO функция = словарь[юзер_выбор]['func']
# TODO функция(параметры)

# TODO Тут можно хитро воспользоваться тем, что input() передает ввод пользователя в строках (str)
# TODO И ключи у нас в словаре строчные '0'...
# TODO Можем просто написать условие while ввод не в словаре
while True:
    user_input = input('Введите желаемую фигуру >')
    user_input = int(user_input)
    if 0 <= user_input <= 3:
        break
    else:
        print("Вы ввели некорректный номер")


def triangle(point, angle=25, length=100):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=length, width=3)
    v3.draw()


def square(point, angle=25, length=100):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=length, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 180, length=length, width=3)
    v3.draw()

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 270, length=length, width=3)
    v4.draw()


def pentagon(point, angle=25, length=100):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 72, length=length, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 144, length=length, width=3)
    v3.draw()

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 216, length=length, width=3)
    v4.draw()

    sd.line(start_point=v4.end_point, end_point=point, width=3)


def hexagon(point, angle=25, length=100):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=length, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 120, length=length, width=3)
    v3.draw()

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 180, length=length, width=3)
    v4.draw()

    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 240, length=length, width=3)
    v5.draw()

    sd.line(start_point=v5.end_point, end_point=point, width=3)


functions = [triangle, square, pentagon, hexagon]
functions[int(user_input)](point=sd.get_point(250, 250), angle=25, length=100)


sd.pause()
