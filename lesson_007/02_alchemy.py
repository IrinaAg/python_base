# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())


class Water:
    def __init__(self):
        self.name = 'Water'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        else:
            isinstance(other, Earth)  # TODO эта строка ничего не делает, хотя лучше бы эту проверку использовать
            # TODO в elif, а в else отправить все неправильные варианты и возвращать None
            return Dirt()

    def __str__(self):
        return self.name


class Air:
    def __init__(self):
        self.name = 'Air'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Water):
            return Storm()
        else:
            isinstance(other, Earth)
            return Dust()

    def __str__(self):
        return self.name


class Fire:
    def __init__(self):
        self.name = 'Fire'

    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()
        elif isinstance(other, Air):
            return Lightning()
        else:
            isinstance(other, Water)
            return Steam()

    def __str__(self):
        return self.name


class Earth:
    def __init__(self):
        self.name = 'Earth'

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Fire):
            return Lava()
        else:
            isinstance(other, Air)
            return Dust()

    def __str__(self):
        return self.name


class Storm:
    def __init__(self):
        self.name = 'Storm'

    def __str__(self):
        return self.name


class Steam:
    def __init__(self):
        self.name = 'Steam'

    def __str__(self):
        return self.name


class Dirt:
    def __init__(self):
        self.name = 'Dirt'

    def __str__(self):
        return self.name


class Lightning:
    def __init__(self):
        self.name = 'Lightning'

    def __str__(self):
        return self.name


class Dust:
    def __init__(self):
        self.name = 'Dust'

    def __str__(self):
        return self.name


class Lava:
    def __init__(self):
        self.name = 'Lava'

    def __str__(self):
        return self.name


print(Water(), '+', Air(), '=', Water() + Air())
print(Water(), '+', Fire(), '=', Water() + Fire())
print(Water(), '+', Earth(), '=', Water() + Earth())
print(Fire(), '+', Air(), '=', Fire() + Air())
print(Air(), '+', Fire(), '=', Air() + Fire())
print(Air(), '+', Earth(), '=', Air() + Earth())
print(Fire(), '+', Earth(), '=', Fire() + Earth())


# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
