#!/usr/bin/env python3
import datetime
import json
import pandas as pd
import re

re_city = re.compile(r'^[\w\-\s]{3,40}$')
re_date = re.compile(r'^(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20)\d\d$')
re_phone_number = re.compile(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]')


# re.findall(r'\d{3}[-\.\s]\d{3}[-\.\s]\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]\d{4}|\d{3}[-\.\s]\d{4}')


def handler_city_dep(text, context):
    match = re.match(re_city, text)
    if match:
        context['city_dep'] = text
        return True
    else:
        return False


def handler_city_arr(text, context):
    match = re.match(re_city, text)
    if match:
        context['city_arr'] = text
        return True
    else:
        return False


def handler_date(text, context):
    matches = re.findall(re_date, text)
    if len(matches) > 0:
        context['handler_date'] = matches[0]
        return True
    else:
        return False


def handler_dispatcher(start='12/28/2020'):  # city_dep, city_arr #datetime.datetime.today()
    month = pd.date_range(start=start, periods=5, freq='7D')
    for day_spb in month:
        fl = []
        fl.append(day_spb)
        # print('Москва - Санкт-Петербург', fl)
        # dict = {'Москва - Санкт-Петербург': day_spb}
        # key = 'рейс Москва - Санкт-Петербург'
        val = day_spb
        # print(key, val)
        flights = [
                  {
                    "рейс Москва - Санкт-Петербург": day_spb,
                  },
                  # {
                  #   "рейс №1 Москва - Казань 01.01.2021", "рейс №2 Москва - Казань 03.01.2021"
                  # }
                ]
        data = {
            'рейс Москва': 'Санкт-Петербург',
            'рейс Санкт-Петербург': 'Казань',
            'flights': {
                'рейс Москва': day_spb,
                # 'рейс Санкт-Петербург': day_kzn,
            },
        }
        print(data['flights'])
        flights.append(day_spb)
        print("рейс Москва - Санкт-Петербург", flights[1])
    week = pd.date_range(start='12/29/2020', periods=5, freq='W')
    # в словаре пользователя (в state.context)
    # можно сделать два ключа
    # по одному - записать рейсы в строку для вывода пользователю
    # 'рейс #1 Москва - Санкт-Петербург 01.01.2021\nрейс #2 Москва - Лондон 01.01.2021...'
    # по второму - хранить рейсы в списке/словаре
    # (или не рейсы, а какие-то ключи, по которым вы сможете найти нужный рейс
    # если данные будут храниться в базе данных - то можно будет хранить какой-нибудь 'id' рейса)
    # пользователь ответит какой-то цифрой или полным названием рейса (в зависимости от того, что вы попросите)
    # и вы этот ответ можете использовать
    # [рейс№1, рейс№2, рейс№3...], пользователь отвечает 1, отнимаем -1 чтобы получить индекс и берем
    # рейсы[0] -> рейс№1

    # Только делать это надо в хэнделрах
    # функция-диспетчер должна выполнять только генерацию данных, можно с записью в json файл или БД
    # (ну и возможно помогать поиск по данным производить)
    # TODO общий принцип понятен, я не понимаю как это все реализовать вот у меня есть 5 рейсов Москва - Санкт-Петербург
    # TODO я не понимаю как в список добавить рейсы Москва-Казань с другой периодичностью.
    # TODO Вы пишите, что данные по рейсам надо записывать
    # TODO в json файл, а как его создать в информации которую я нашла в уже готовый json-файл идет запись.
    for day_kzn in week:
        dict1 = {'Москва': {
            'Казань': [day_kzn]}}
        print(dict1['Москва']['Казань'][0])

handler_dispatcher()

def handler_flight(text, context):
    matches = re.findall(re_date, text)
    if len(matches) > 0:
        context['flight'] = matches[0]
        return True
    else:
        return False


def handler_phone_number(text, context):
    matches = re.findall(re_phone_number, text)
    if len(matches) > 0:
        context['phone_number'] = matches[0]
        return True
    else:
        return False
