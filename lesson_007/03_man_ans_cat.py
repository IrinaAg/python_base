# -*- coding: utf-8 -*-

from random import randint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

from random import randint


# Реализуем модель человека.
# Человек может есть, работать, играть, ходить в магазин.
# У человека есть степень сытости, немного еды и денег.
# Если сытость < 0 единиц, человек умирает.
# Человеку надо прожить 365 дней.
from termcolor import cprint


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None
        self.cat = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_mtv(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def shopping_cat_food(self):
        if self.house.cat_food <= 10:
            cprint('{} сходил в магазин за едой коту'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.cat_food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def clean_house(self):
        cprint('{} убрался в доме'.format(self.name), color='blue')
        self.fullness -= 20
        self.house.dirt -= 100

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} вьехал в дом'.format(self.name), color='cyan')

    def pick_up(self, cat):
        cprint('{} подобрал кота'.format(self.name), color='cyan')
        self.cat = cat
        # TODO 1) Не хватает ещё одного действия, добавления коту своего дома. Для этого надо изменить атрибут кот.хаус
        # TODO на селф.хаус
        # TODO 2) Вместо простой переменной у человека self.cat лучше создать список-атрибут и добавлять кота туда.
        # TODO Чтобы в итоге можно было несколько котов подряд добавить

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 50:
            self.eat()
        elif self.house.food < 20:
            self.shopping()
        elif self.house.cat_food < 10:
            self.shopping_cat_food()
        elif self.house.money < 50:
            self.work()
        elif self.house.dirt > 105:
            self.clean_house()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.work()
        else:
            self.watch_mtv()


class House:

    def __init__(self):
        self.food = 50
        self.money = 50
        self.cat_food = 0
        self.dirt = 0

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}, еды для кота {}'.format(self.food, self.money, self.cat_food)


class Cat:

    def __init__(self, name, house):
        self.name = name
        self.fullness = 50
        self.house = house

    def __str__(self):
        return 'Я - {}, сытость {}'.format(self.name, self.fullness)

    def eat(self):
        if self.house.cat_food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.cat_food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def sleeping(self):
        cprint('{} спит'.format(self.name), color='blue')
        self.fullness -= 10

    def pulls_wallpaper(self):
        cprint('{} дерет обои'.format(self.name), color='green')
        self.fullness -= 10
        self.house.dirt += 5

    def cat_act(self) -> object:
        if self.fullness < 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif dice == 1:
            self.sleeping()
        elif dice == 2:
            self.eat()
        else:
            self.pulls_wallpaper()


my_sweet_home = House()
my_pet = Cat(name='Котик', house=my_sweet_home)


citizens = [
    Man(name='Человек')
]

pets = [
    Cat(name='Котик', house=my_sweet_home)
]


for citizen in citizens:
    citizen.go_to_the_house(house=my_sweet_home)
    citizen.pick_up(cat=my_pet)


for day in range(1, 366):
    print('================ день {} =================='.format(day))
    for citizen in citizens:
        citizen.act()
    for pet in pets:
        pet.cat_act()
    print('--- в конце дня ---')
    for citizen in citizens:
        print(citizen)
    for pet in pets:
        print(pet)
    print(my_sweet_home)


# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
