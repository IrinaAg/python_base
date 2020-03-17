import simple_draw as sd
import random

N = 20

snowflakes = []
drift = []

for _ in range(N):
    x = sd.random_number(0, 120)
    y = sd.random_number(620, 650)
    size = sd.random_number(10, 30)
    snowflakes.append([x, y, size])


while True:
    sd.start_drawing()
    for i, snowflake in enumerate(snowflakes):
        point = sd.get_point(snowflake[0], snowflake[1])
        sd.snowflake(center=point, color=sd.background_color, length=snowflake[2])
        snowflake[1] -= 35
        if snowflake[1] <= 50:
            drift.append(i)
        # snowflake[0] += 5
        point = sd.get_point(snowflake[0], snowflake[1])
        sd.snowflake(center=point, color=sd.COLOR_WHITE, length=snowflake[2])
    drift.reverse()
    for index in drift:
        snowflakes.pop(index)
    drift = []
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

# sd.pause()
