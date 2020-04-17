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

    def can_fall(self) -> object:
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
    fallen_flakes = []  # TODO в данной реализации вы не используете список упавших снежинок
    count = 0
    for flake in flakes:
        if not flake.can_fall():
            count += 1
            fallen_flakes.append(Snowflake())  # TODO К тому же стоило бы собирать индексы упавших снежинок
            # TODO А вы создаете новые объекты-снежинки, которые никак не связаны с упавшими.
    # print(count)
    # print(fallen_flakes)
    return count
# TODO Поступить можно 2 способами
# TODO Простой - убрать список упавших снежинок, оставить счётчик
# TODO Но тогда нужно изменить метод move, чтобы он двигал снежинки, только если они не вышли за границу экрана
# TODO Сложный - собирать в список индексы снежинок. Добавить метод, который будет принимать этот список,
# TODO разворачивать и запускать по нему цикл, чтобы по индексам удалять объекты-снежинки из списка flakes

def append_flakes(count):  # TODO Кстати здесь вы передаете число, но никак его не используете
    # TODO Стоит добавить цикл, который будет повторять добавление снежинок count-раз
    flakes.append(Snowflake())
    # print(flakes)


while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        append_flakes(count=fallen_flakes)  # добавить еще сверху
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
