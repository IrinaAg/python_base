# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Каждая запись отображает сколько и по какой цене закупалось товаров.
#
# Задание: вывести суммарную стоимость каждого ВИДА товара на складе c помощью циклов
#
# Формат вывода:
#   <товар_1> - <кол-во_товара_1> шт, стоимость <общая_стоимость_товара_1> руб
#   <товар_2> - <кол-во_товара_2> шт, стоимость <общая_стоимость_товара_2> руб
#   <товар_4> - <кол-во_товара_3> шт, стоимость <общая_стоимость_товара_3> руб
#
# Например:
#   Стул - 1111 шт, стоимость 8888 руб
#   Диван - 2222 шт, стоимость 9999 руб
#   и так далее
#
# Алгоритм должен получиться приблизительно такой:
#
# цикл for по товарам с получением кода и названия товара
#     инициализация переменных для подсчета количества и стоимости товара
#     получение списка на складе по коду товара
#     цикл for по списку на складе
#         подсчет количества товара
#         подсчет стоимости товара
#     вывод на консоль количества и стоимости товара на складе


for key in goods:
    print(goods[key])
    cost = 0
    quantity = 0
    #lst_good = []
    #lst_good.extend(goods) #список товаров
    #print(lst_good)
    for key, val in store.items():
        print(val)
        #print(store[key][0]['quantity'])




        #lamps_cost = store['12345'][0]['quantity'] * store['12345'][0]['price']  #TODO не понимаю как можно в цикле посчитать кол-во и
        #table_sum_quantity = store['23456'][0]['quantity'] + store['23456'][1]['quantity']      # стоимость товара
        #table_cost = store['23456'][0]['quantity'] * store['23456'][0]['price']
        #table_cost1 = store['23456'][1]['quantity'] * store['23456'][1]['price']
        #table_cost_sum = table_cost + table_cost1


#print(lst_good[0], '-', store['12345'][0]['quantity'], 'шт', 'стоимость', lamps_cost, 'руб')
#print(lst_good[1], '-', table_sum_quantity, 'шт', 'стоимость', table_cost_sum, 'руб')




