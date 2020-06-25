# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


# def get_prime_numbers(n):
#     prime_numbers = []
#     for number in range(2, n + 1):
#         for prime in prime_numbers:
#             if number % prime == 0:
#                 break
#         else:
#             prime_numbers.append(number)
#     return prime_numbers


# for number in get_prime_numbers(n=100):
#     print(number)

# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


class PrimeNumbers:

    def __init__(self, n):
        self.prime_numbers = []
        self.n = n
        self.i = 0

    def __iter__(self):
        self.i = 1
        return self

    def get_prime_numbers(self):
        self.i += 1
        for prime in self.prime_numbers:
            if self.i % prime == 0:
                return False
        return True

    def __next__(self):
        while self.i < self.n:
            if self.get_prime_numbers():
                self.prime_numbers.append(self.i)
                return self.i
        else:
            raise StopIteration()


prime_number_iterator = PrimeNumbers(n=10000)


# for number in prime_number_iterator:
#     print(number)


# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


def get_prime_numbers(i):
    if i == 1:
        return False
    for x in range(2, i):
        if i % x == 0:
            return False
    return True


#
# def prime_numbers_generator(i=1, n=10000):
#     while i < n:
#         if get_prime_numbers(i):
#             yield i
#         i += 1


# prime_number_generator = PrimeNumbers(n=10000)
# for number in prime_number_generator:
#     print(number)

# for number_g, number_i in zip(prime_numbers_generator(n=10000), prime_number_iterator):
#     print(number_g == number_i)


# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True


def sum_digits(i):
    middle = len(str(i)) // 2
    if middle == 0 or str(i)[:middle] == str(i)[-middle:]:
        return True
    if len(str(i)) > 3:
        for _ in range(i):
            num = list(str(i))
            if int(num[0]) + int(num[1]) == int(num[2]) + int(num[3]):
                return True
    else:
        return False


def prime_numbers_generator(i=1, n=10000, func_filter1=get_prime_numbers, func_filter2=sum_digits):
    while i < n:
        if func_filter1(i) and func_filter2(i):
            yield i
        i += 1


for number in prime_numbers_generator(n=10000):
    print(number)

# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101

# def palindrom(i):
#         return str(i) == str(i)[::-1]
#
#
# def prime_numbers_generator(i=1, n=10000):
#     while i < n:
#         if get_prime_numbers(i) and palindrom(i):
#             yield i
#         i += 1
#
#
# for number in prime_numbers_generator(n=10000):
#     print(number)

# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.
#зачёт!