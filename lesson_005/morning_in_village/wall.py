import simple_draw as sd


def wall(x, y):
    for row, x in enumerate(range(150, 500, 10)):
        y0 = 0 if row % 2 else - 10
        for y in range(y0, 360, 20):
            point_start = sd.get_point(x, y)
            point_end = sd.get_point(x + 20, y + 10)
            sd.rectangle(left_bottom=point_start, right_top=point_end, color=sd.COLOR_ORANGE, width=1)


wall(x=0, y=0)

# sd.pause()