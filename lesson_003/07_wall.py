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


for i, y in enumerate(range(y, wall_length, step_y)):
    for x in range(0, wall_length, step_x):
        if i % 2 == 0:  # TODO Хорошо, но обратите внимание, что изменений на самом деле не так много
            point_start = sd.get_point(x0, y)  # TODO Эту строку и следующие
            point_end1 = sd.get_point(x + step_x, y + step_y)
            sd.rectangle(left_bottom=point_start, right_top=point_end1, color=sd.COLOR_ORANGE, width=1)
        else:
            point_start = sd.get_point(x0 - 50, y)
            point_end = sd.get_point(x + (step_x * 0.5), y + step_y)  # TODO Можно сделать одинаковыми
            # TODO И поставить после блока if/else
            # TODO А внутри if/else - изменять только x0
            sd.rectangle(left_bottom=point_start, right_top=point_end, color=sd.COLOR_ORANGE, width=1)

sd.pause()
