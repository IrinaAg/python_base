import simple_draw as sd

radius = 60
eye = radius // 7


def smile(color):
    eye_left = sd.get_point(point.x - 25, point.y + 20)
    eye_right = sd.get_point(point.x + 25, point.y + 20)
    start_point = sd.get_point(point.x - 45, point.y - 10)
    end_point = sd.get_point(point.x - 25, point.y - 30)
    start_point1 = sd.get_point(point.x - 25, point.y - 30)
    end_point1 = sd.get_point(point.x + 20, point.y - 30)
    start_point2 = sd.get_point(point.x + 20, point.y - 30)
    end_point2 = sd.get_point(point.x + 40, point.y - 10)
    sd.circle(center_position=point, radius=radius, width=2, color=color)
    sd.circle(center_position=eye_left, radius=eye, width=0, color=color)
    sd.circle(center_position=eye_right, radius=eye, width=0, color=color)
    sd.line(start_point=start_point, end_point=end_point, color=color, width=2)
    sd.line(start_point=start_point1, end_point=end_point1, color=color, width=2)
    sd.line(start_point=start_point2, end_point=end_point2, color=color, width=2)


point = sd.get_point(325, 175)
smile(color=sd.COLOR_BLACK)


# sd.pause()
