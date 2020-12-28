#!/usr/bin/env python3
import datetime
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


def dispatcher(start='12/28/2020'):  # city_dep, city_arr #datetime.datetime.today()
    month = pd.date_range(start=start, periods=5, freq='7D')
    for day_spb in month:
        # dict = {'Москва - Санкт-Петербург': day_spb}
        key = 'рейс Москва - Санкт-Петербург'
        val = day_spb
        print(key, val)
    week = pd.date_range(start='12/29/2020', periods=5, freq='W')
    # Мне не понятно как в один словарь поместить два
    # и более рейса или должны быть разные словари?
    # И как потом извлекать по ключу данные из них, как функция поймет,
    # что написал пользователь?
    # Или должен быть сценарий с ветвлением изначально если город один то этот шаг если другой
    # город, то проскакиваем первый город?
    # TODO в словаре пользователя (в state.context)
    # TODO можно сделать два ключа
    # TODO по одному - записать рейсы в строку для вывода пользователю
    # TODO 'рейс #1 Москва - Санкт-Петербург 01.01.2021\nрейс #2 Москва - Лондон 01.01.2021...'
    # TODO по второму - хранить рейсы в списке/словаре
    # TODO (или не рейсы, а какие-то ключи, по которым вы сможете найти нужный рейс
    # TODO если данные будут храниться в базе данных - то можно будет хранить какой-нибудь 'id' рейса)
    # TODO пользователь ответит какой-то цифрой или полным названием рейса (в зависимости от того, что вы попросите)
    # TODO и вы этот ответ можете использовать
    # TODO [рейс№1, рейс№2, рейс№3...], пользователь отвечает 1, отнимаем -1 чтобы получить индекс и берем
    # TODO рейсы[0] -> рейс№1

    # TODO Только делать это надо в хэнделрах
    # TODO функция-диспетчер должна выполнять только генерацию данных, можно с записью в json файл или БД
    # TODO (ну и возможно помогать поиск по данным производить)
    for day_kzn in week:
        dict1 = {'Москва': {
            'Казань': [day_kzn]}}
        print(dict1['Москва']['Казань'][0])


dispatcher()


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
