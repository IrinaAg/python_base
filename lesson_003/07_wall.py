# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

x, y = 0, 0
step_y = 50
step_x = 100
wall_length = 600
i = 0

for i, y in enumerate(range(y, wall_length, step_y)):
    i += 1  # TODO Эта операция не нужна, i и так считается с помощью enumerate
    for x in range(0, wall_length, step_x):
        if i % 2 == 0:  # TODO Это верный ход, но можно использовать его эффективнее
            # TODO С помощью этой проверки создавайте переменную x0, которая в одном случае будет равна 0
            # TODO А в другом случае -50
            # TODO С этой переменной и начинается цикл по x
            point_start = sd.get_point(step_x - step_x, y)
            point_end1 = sd.get_point(x + step_x, y + step_y)
            sd.rectangle(left_bottom=point_start, right_top=point_end1, color=sd.COLOR_ORANGE, width=1)
        else:
            point_start = sd.get_point(x - 50, y)
            point_end = sd.get_point(x + (step_x * 0.5), y + step_y)
            sd.rectangle(left_bottom=point_start, right_top=point_end, color=sd.COLOR_ORANGE, width=1)


sd.pause()
