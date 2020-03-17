import simple_draw as sd
import random


def tree(point, angle, length):
    if length < 3:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
    v1.draw()
    next_point = v1.end_point
    next_angle = angle + sd.random_number(18, 42)
    next_length = length * random.uniform(.6, .9)
    next_angle_left = angle - sd.random_number(18, 42)
    tree(point=next_point, angle=next_angle, length=next_length)
    tree(point=next_point, angle=next_angle_left, length=next_length)


point_0 = sd.get_point(950, 0)
root_point = sd.get_point(300, 30)
tree(point=point_0, angle=90, length=105)


# sd.pause()
