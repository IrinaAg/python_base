# Составить отдельный модуль mastermind_engine, реализующий функциональность игры.
# В этом модуле нужно реализовать функции:
#   загадать_число()
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
# Загаданное число хранить в глобальной переменной.
# Обратите внимание, что строки - это список символов.
import random


def get_all_answer():
    ans = []
    for i in range(10000):
        tmp = str(i).zfill(4)
        if len(set(map(int, tmp))) == 4:  # TODO Тут ещё надо проверить, чтобы 0 не попадал на первое место
            ans.append(list(map(int, tmp)))
    return ans


def get_one_answer(ans):
    one = random.choice(ans)
    return one


def check(nums, one):
    bulls, cows = 0, 0
    for i, num in enumerate(nums):
        if num in one:
            if nums[i] == one[i]:
                bulls += 1
            else:
                cows += 1
    return bulls, cows

