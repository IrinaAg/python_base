import simple_draw as sd

sd.resolution = (1200, 800)
rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
x1, y1 = 1200, 35
# radius = 550
width = 15


def rainbow(radius):
    for i, rainbow_color in enumerate(rainbow_colors):
        radius += 15
        start = sd.get_point(x1, y1)
        sd.circle(center_position=start, radius=radius, color=rainbow_color, width=15)


rainbow(radius=550)

# sd.pause()
