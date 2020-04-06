# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
import simple_draw as sd

snowflakes = []
drift = []
N = 20


def create_snowflakes():
    for snowflake in range(N):
        x = sd.random_number(5, 550)
        y = sd.random_number(620, 650)
        size = sd.random_number(10, 30)
        snowflakes.append([x, y, size])


def draw_snowflakes_color(color=sd.COLOR_WHITE):
    for i, snowflake in enumerate(snowflakes):
        point = sd.get_point(snowflakes[i][0], snowflakes[i][1])
        sd.snowflake(center=point, color=color, length=snowflakes[i][2])


def shift_snowflakes():
    for i, snowflake in enumerate(snowflakes):
        snowflakes[i][1] -= sd.random_number(0, 25)
        snowflakes[i][0] += sd.random_number(-15, 15)


def screen_reach_numbers():
    for i, snowflake in enumerate(snowflakes):
        if snowflakes[i][1] <= 15:
            drift.append(i)
            print(drift)
        drift.reverse()
    return drift


def remove_snowflakes():
    for index in drift:
        snowflakes.pop(index)
    return drift