# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПРОЦЕССНОМ стиле
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
#

import multiprocessing
from os import listdir, path
from utils import time_track, VolatilityPrint
from queue import Empty


store = {}
trades = {}
file_path = 'trades'


class TickerVolatility(multiprocessing.Process):

    def __init__(self, file_name, collector, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file_name = file_name
        self.collector = collector

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
        # store[ticker_name] = (round(volatility, 2))
        self.collector.put({ticker_name: round(volatility, 2)})
        # sizers=[TickerVolatility(file_name=self.file_name, collector=self.collector)]
        # while True:
        #     try:
        #         ticker = self.collector.get(timeout=0.1)
        #         trades.update(ticker)
        #     except Empty:
        #         if not any(sizer.is_alive() for sizer in sizers):
        #             break


@time_track
def main():
    collector = multiprocessing.Queue()
    sizers = [TickerVolatility(path.join(file_path, file_name), collector=collector) for file_name in listdir(file_path)]

    for sizer in sizers:
        sizer.start()

    while True:
        try:
            ticker = collector.get(timeout=0.1)
            trades.update(ticker)
        except Empty:
            if not any(sizer.is_alive() for sizer in sizers):
                break

    for sizer in sizers:
        sizer.join()

    proc = VolatilityPrint(trades)
    proc.print()


if __name__ == '__main__':
    main()

