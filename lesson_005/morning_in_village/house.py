import simple_draw as sd

from lesson_005.morning_in_village.wall import wall


def square(left_bottom, side, color, width):
    sd.square(left_bottom=left_bottom, side=side, color=color, width=width)


def polygon(point_list, color, width):
    sd.polygon(point_list=point_list, color=color, width=width)


def ellipse(left_bottom, right_top, color, width):
    sd.ellipse(left_bottom=left_bottom, right_top=right_top, color=color, width=width)


wall(x=0, y=0)

square(left_bottom=sd.get_point(150, 0), side=360, color=sd.COLOR_ORANGE, width=3)

square(left_bottom=sd.get_point(230, 80), side=200, color=sd.COLOR_DARK_GREEN, width=0)

point_list = [sd.get_point(150, 361), sd.get_point(510, 361), sd.get_point(330, 520)]
polygon(point_list=point_list, color=sd.COLOR_DARK_GREEN, width=0)

ellipse(left_bottom=sd.get_point(300, 400), right_top=sd.get_point(350, 450), color=sd.COLOR_GREEN, width=0)

# sd.pause()
