# -*- coding: utf-8 -*-

import simple_draw as sd

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


# class Snowflake:
#
#     def __init__(self):
#         self.x = sd.random_number(5, 550)
#         self.y = sd.random_number(550, 600)
#         self.size = sd.random_number(10, 30)
#
#
#     def clear_previous_picture(self):
#         point = sd.get_point(self.x, self.y)
#         sd.snowflake(center=point, color=sd.background_color, length=self.size)
#
#     def move(self):
#         self.y -= sd.random_number(0, 25)
#         self.x += sd.random_number(-15, 15)
#
#     def draw(self):
#         point = sd.get_point(self.x, self.y)
#         sd.snowflake(center=point, color=sd.COLOR_WHITE, length=self.size)
#
#     def can_fall(self):
#         return self.y > 15
#
#
# flake = Snowflake()
#
# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:

# вариант без удаления снежинок

# class Snowflake:
#
#     def __init__(self):
#         self.x = sd.random_number(5, 550)
#         self.y = sd.random_number(550, 600)
#         self.size = sd.random_number(10, 30)
#
#     def clear_previous_picture(self):
#         point = sd.get_point(self.x, self.y)
#         sd.snowflake(center=point, color=sd.background_color, length=self.size)
#
#     def move(self):
#         if self.y > 15:
#             self.y -= sd.random_number(0, 25)
#             self.x += sd.random_number(-15, 15)
#
#     def draw(self):
#         point = sd.get_point(self.x, self.y)
#         sd.snowflake(center=point, color=sd.COLOR_WHITE, length=self.size)
#
#     def can_fall(self):
#         return self.y > 15
#
#
# N = 20
#
#
# def get_flakes(count):
#     count = 0
#     flakes = []
#     for _ in range(N):
#         flakes.append(Snowflake())
#         count += 1
#     return flakes
#
#
# flakes = get_flakes(count=N)  # создать список снежинок
#
#
# def get_fallen_flakes():
#     count = 0
#     for flake in flakes:
#         if not flake.can_fall():
#             count += 1
#     return count
#
#
# def append_flakes(count):
#     flakes.append(Snowflake())
#     return flakes
#
#
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break


class Snowflake:

    def __init__(self):
        self.x = sd.random_number(5, 550)
        self.y = sd.random_number(550, 600)
        self.size = sd.random_number(10, 30)

    def clear_previous_picture(self):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, color=sd.background_color, length=self.size)

    def move(self):
        self.y -= sd.random_number(0, 25)
        self.x += sd.random_number(-15, 15)

    def draw(self):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, color=sd.COLOR_WHITE, length=self.size)

    def can_fall(self):
        return self.y > 15


N = 20


def get_flakes(count):
    count = 0
    flakes = []
    for _ in range(N):
        flakes.append(Snowflake())
        count += 1
    # print(count)
    # print(flakes)
    return flakes


flakes = get_flakes(count=N)  # создать список снежинок


def get_fallen_flakes():
    fallen_flakes = []
    count = 0
    for i, flake in enumerate(flakes):
        if not flake.can_fall():
            count += 1
            fallen_flakes.append(i)
    # print(count)
    print(fallen_flakes)
    return count


def remove_flakes(fallen_flakes):
    fallen_flakes.reverse() # TODO не разворачивается список с индексами упавших снежинок
    for index in fallen_flakes:
        flakes.pop(index)
    return fallen_flakes


def append_flakes(count):
    for _ in flakes:
        flakes.append(count)
    print(flakes)
    print(count)


while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        remove_flakes(fallen_flakes)
        append_flakes(count=fallen_flakes)  # добавить еще сверху
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
