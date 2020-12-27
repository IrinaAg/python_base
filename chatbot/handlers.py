#!/usr/bin/env python3
import datetime
import pandas as pd
import re


re_city = re.compile(r'^[\w\-\s]{3,40}$')
re_date = re.compile(r'^(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20)\d\d$')
re_phone_number = re.compile(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]') #re.findall(r'\d{3}[-\.\s]\d{3}[-\.\s]\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]\d{4}|\d{3}[-\.\s]\d{4}')


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


def dispatcher(start='12/28/2020'):#city_dep, city_arr #datetime.datetime.today()
    month = pd.date_range(start=start,periods=5, freq='7D')
    for day_spb in month:
        # dict = {'Москва - Санкт-Петербург': day_spb}
        key = 'рейс Москва - Санкт-Петербург'
        val = day_spb
        print(key, val)
    week = pd.date_range(start='12/29/2020',periods=5, freq='W') #TODO Мне не понятно как в один словарь поместить два
    #TODO и более рейса или должны быть разные словари? И как потом извлекать по ключу данные из них, как функция поймет,
    #TODO что написал пользователь? Или должен быть сценарий с ветвлением изначально если город один то этот шаг если другой
    #TODO город, то проскакиваем первый город?
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
