# -*- coding: utf-8 -*-

# Написать декоратор, который будет логировать (записывать в лог файл)
# ошибки из декорируемой функции и выбрасывать их дальше.
#
# Имя файла лога - function_errors.log
# Формат лога: <имя функции> <параметры вызова> <тип ошибки> <текст ошибки>
# Лог файл открывать каждый раз при ошибке в режиме 'a'


def log_errors(func):
    def surrogate(*args, **kwargs):
        try:
            func(*args, **kwargs)  # TODO результат работы функкции надо вернуть через return
        except ValueError as exc:
            file = open('function_errors.log', 'a', encoding='utf8')
            print(func.__name__, *args, 'ValueError', exc, file=file)
            # TODO Тут тоже надо закрыть файл (или использовать with)
            # TODO + надо и тут и ниже добавить raise. Поймали ошибку, записали, выпустили дальше
            # ошибки из декорируемой функции и выбрасывать их дальше.
        except ZeroDivisionError:
            file = open('function_errors.log', 'a', encoding='utf8')
            print(func.__name__, *args, 'ZeroDivisionError', 'division by zero', file=file)
            file.close()

    return surrogate


# Проверить работу на следующих функциях
@log_errors
def perky(param):
    return param / 0


@log_errors
def check_line(line):
    name, email, age = line.split(' ')
    if not name.isalpha():
        raise ValueError("it's not a name")
    if '@' not in email or '.' not in email:
        raise ValueError("it's not a email")
    if not 10 <= int(age) <= 99:
        raise ValueError('Age not in 10..99 range')


lines = [
    'Ярослав bxh@ya.ru 600',
    'Земфира tslzp@mail.ru 52',
    'Тролль nsocnzas.mail.ru 82',
    'Джигурда wqxq@gmail.com 29',
    'Земфира 86',
    'Равшан wmsuuzsxi@mail.ru 35',
]
for line in lines:
    try:
        check_line(line)
    except Exception as exc:
        print(f'Invalid format: {exc}')
perky(param=42)

# Усложненное задание (делать по желанию).
# Написать декоратор с параметром - именем файла
#
# @log_errors('function_errors.log')
# def func():
#     pass
