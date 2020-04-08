# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

from snowfall import create_snowflakes, draw_snowflakes_color, shift_snowflakes, remove_snowflakes, screen_reach_numbers

# создать_снежинки(N)
create_snowflakes()

while True:
    sd.start_drawing()
    #  нарисовать_снежинки_цветом(color=sd.background_color)
    draw_snowflakes_color(color=sd.background_color)
    #  сдвинуть_снежинки()
    shift_snowflakes()
    #  нарисовать_снежинки_цветом(color)
    draw_snowflakes_color()
    #  если есть номера_достигших_низа_экрана() то
    if screen_reach_numbers():
        #       удалить_снежинки(номера)
        remove_snowflakes()
    #       создать_снежинки(count)
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

#Зачет!