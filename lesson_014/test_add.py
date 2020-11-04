# Наш фрейм
x = ['X-', 'X-', '34', '4/', '21']


def add_strike_points(frames, index):  # TODO Напишем отдельно для страйка, отдельно для спэра
    result = 0
    throw = 0
    for _ in range(2):
        if index >= len(frames):
            break

        cur_frame = frames[index + 1]
        if cur_frame[throw] == 'X':
            result += 10
            index += 1
        elif cur_frame[throw].isdigit():
            result += int(cur_frame[throw])
            throw += 1
        elif cur_frame[throw] == '/':
            result += 10
    return result


print(add_strike_points(x, 0))