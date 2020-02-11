# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

x, y = 0, 0
x0 = 0
step_y = 50
step_x = 100
wall_length = 600

#
# for i, y in enumerate(range(y, wall_length, step_y)):
#     for x in range(0, wall_length, step_x):
#         if i % 2 == 0:
#             x0 = 0
#         else:
#             x0 = x - 50
#             x = x + (step_x * 0.5)
#         point_start = sd.get_point(x, y)
#         point_end = sd.get_point(x + step_x, y + step_y)
#         sd.rectangle(left_bottom=point_start, right_top=point_end, color=sd.COLOR_ORANGE, width=1)

for row, y in enumerate(range(y, wall_length, step_y)):
    x0 = 0 if row % 2 else - 50
    for x in range(x0, wall_length, step_x):
        point_start = sd.get_point(x, y)
        point_end = sd.get_point(x + step_x, y + step_y)
        sd.rectangle(left_bottom=point_start, right_top=point_end, color=sd.COLOR_ORANGE, width=1)

sd.pause()
#зачет!