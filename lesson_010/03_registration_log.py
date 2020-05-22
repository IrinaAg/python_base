# -*- coding: utf-8 -*-
import logging


# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.


class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


good_file = open('registrations_good.log', 'a', encoding='utf8')
bad_file = open('registrations_bad.log', 'a', encoding='utf8')


def check(line):
    if len(line.split(' ')) != 3:
        raise ValueError('НЕ присутсвуют все три поля')
    name, email, age = line.split(' ')
    name = str(name)
    email = str(email)
    if age.isdigit() is False:
        raise ValueError('поле возраст НЕ является числом')
    age = int(age)
    if not name.isalpha():
        raise NotNameError('Ошибка в имени')
    elif '@' not in email or '.' not in email:
        raise NotEmailError('Поле е-мейл НЕ содержит @ и .')
    elif not 10 <= age <= 99:
        raise ValueError('поле возраст НЕ является числом от 10 до 99')
    else:
        return


with open('registrations.txt', 'r') as ff:
    for line in ff:
        line = line[:-1]
        try:
            check(line)
            print(line, file=good_file)
        except ValueError as exc:
            print(line, exc, file=bad_file)
        except NotNameError:
            print(f'Ошибка в имени в строке {line}', file=bad_file)
        except NotEmailError:
            print(f'Поле е-мейл НЕ содержит @ и . в строке {line}', file=bad_file)
    good_file.close()
    bad_file.close()
#зачет!