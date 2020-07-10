# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
#
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.

import threading
from os import listdir, path
from utils import time_track, VolatilityPrint
import time

store = {}
trades = {}
file_path = 'trades'


class TickerVolatility(threading.Thread):

    def __init__(self, file_name, *args, **kwargs):
        super().__init__(**kwargs)
        self.file_name = file_name

    def run(self):
        ticker_name = path.basename(self.file_name).split('_')[1].split('.')[0]
        results = []
        with open(self.file_name, 'r') as f:
            for line in f:
                if line.startswith('SECID'):
                    continue
                else:
                    results.append(float(line.split(',')[2]))
        results = sorted(results)
        half_sum = (results[0] + results[-1]) / 2
        volatility = (results[-1] - results[0]) / half_sum * 100
        store[ticker_name] = (round(volatility, 2))
        # TODO 1) С внешними переменными работать не очень здорово, стоит хотя бы параметром сюда передавать словарь
        # TODO 2) Подобный способ, с обращением к одному словарю из нескольких потоков, может вести к потерям,
        # TODO если операции записи будут не атомарными.
        # TODO Как вариант - можно создать атрибут-переменную и туда записывать волатильность.
        # TODO А после всех расчётов - пройти циклом по объектам и собрать данные из атрибутов.
        # TODO Либо можно использовать разные типы блокировщиков.


@time_track
def main():
    sizers = [TickerVolatility(path.join(file_path, file_name)) for file_name in listdir(file_path)]

    for sizer in sizers:
        sizer.start()
        # time.sleep(0.001)
        if sizer.is_alive():
            sizer.need_stop = True
    for sizer in sizers:
        sizer.join()

    proc = VolatilityPrint(store)
    proc.print()


if __name__ == '__main__':
    main()
