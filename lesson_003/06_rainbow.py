# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)


# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
x, y = 50, 50
angle = 45
lenght = 700
width = 4
step = 5


for x, item in enumerate(rainbow_colors):
    x += (width + step)
    y += (width + step)
    start = sd.get_point(x, y)
    sd.vector(start, angle, lenght, color=item, width=width)


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
x1, y1 = 380, -15
radius = 420
width = 15


for i, item in enumerate(rainbow_colors):
    radius += 15
    start = sd.get_point(x1, y1)
    sd.circle(center_position=start, radius=radius, color=item, width=width)

sd.pause()
#зачет!