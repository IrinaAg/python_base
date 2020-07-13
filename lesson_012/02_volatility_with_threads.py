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
from collections import defaultdict


class TickerVolatility(threading.Thread):

    def __init__(self, file_name, lock, *args, **kwargs):
        super().__init__(**kwargs)
        self.file_name = file_name
        self.lock = lock

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
        self.lock.acquire()
        store[ticker_name] = (round(volatility, 2))
        self.lock.release()


store = defaultdict(int)


@time_track
def main():
    lock = threading.Lock()
    file_path = 'trades'
    sizers = [TickerVolatility(path.join(file_path, file_name), lock=lock) for file_name in listdir(file_path)]

    for sizer in sizers:
        sizer.start()
        if sizer.is_alive():
            sizer.need_stop = True

    for sizer in sizers:
        sizer.join()

    proc = VolatilityPrint(store)
    proc.print()


if __name__ == '__main__':
    main()
