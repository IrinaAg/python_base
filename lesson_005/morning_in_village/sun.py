import simple_draw as sd


def circle(center_position, radius, color, width=0):
    sd.circle(center_position=center_position, radius=radius, color=color, width=width)


def vector(start, angle, length, color, width):
    sd.vector(start=start, angle=angle, length=length, color=color, width=width)


circle(center_position=sd.get_point(700, 700), radius=50, color=sd.COLOR_YELLOW, width=0)

for angle in range(0, 361 - 20, 20):
    vector(start=sd.get_point(700, 700), angle=angle, length=65, color=sd.COLOR_YELLOW, width=1)

# sd.pause()
