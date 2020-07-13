import time


def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()

        result = func(*args, **kwargs)

        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f'Функция работала {elapsed} секунд(ы)')
        return result
    return surrogate


class VolatilityPrint():
    def __init__(self, store):
        self.store = store

    def print(self):
        print('Максимальная волатильность:')
        view = sorted(self.store.items(), key=lambda elem: elem[1], reverse=True)
        for ticker, value in view[:3]:
            print(f'       {ticker} - {value}%')
        print('Минимальная волатильность:')
        view = [(ticker, vol) for ticker, vol in view if vol > 0]
        for ticker, value in view[-3:]:
            print(f'       {ticker} - {value}%')
        print('Нулевая волатильность:')
        zeroes = [ticker for ticker, vol in self.store.items() if vol == 0]
        print(f'       {", ".join(sorted(zeroes))}')