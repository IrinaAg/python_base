import datetime
import pandas as pd


def dispatcher(start='12/23/2020'):#city_dep, city_arr #datetime.datetime.today()
    month = pd.date_range(start=start,periods=5, freq='7D')
    for day_spb in month:
        dict = {'Москва': {
                'Санкт-Петербург': [day_spb]}}
        # print(dict['Москва']['Санкт-Петербург'][0])
        list_of_dates = []
        list_of_dates.append(dict['Москва']['Санкт-Петербург'][0])
        print(list_of_dates[0])
    week = pd.date_range(start='12/25/2020',periods=5, freq='W')
    for day_kzn in week:
        dict1 = {'Москва': {
                'Казань': [day_kzn]}}
        print(dict1['Москва']['Казань'][0])


dispatcher()
