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


def check(line):
    file = open('registrations_good.log', 'a', encoding='utf8')  # TODO Файл открывать нужно вне цикла
    # TODO До разделения на 3 переменные нужно сперва проверить len(line.split(' ')) != 3
    # TODO Если длина не равна 3 - вызывать исключения
    name, email, age = line.split(' ')
    name: str = str(name)
    email = str(email)
    # TODO Перед int(age) надо сперва проверить age.isdigit()
    # TODO если ответ False - то raise
    age = int(age)
    if not name.isalpha():
        raise NotNameError
    elif '@' not in email or '.' not in email:
        raise NotEmailError
    elif not 10 <= age <= 99:
        raise ValueError
    else:
        print(line, file=file)  # TODO тут не принт, а просто return
        file.close()


with open('registrations.txt', 'r') as ff:
    # TODO для этих файлов (логов) используйте один тип открытия, либо open, либо logging
    # TODO Лучше open, тк логгинг пока не проходили
    logging.basicConfig(filename="registrations_bad.log", level=logging.ERROR)
    for line in ff:
        line = line[:-1]
        try:
            check(line)
            # TODO А здесь уже запись производить
        except ValueError as exc:
            if 'unpack' in exc.args:  # TODO С теми двумя проверками выше - этот блок if/else не нужен будет
                # TODO Уточняющее сообщение можно в ошибку добавить ValueError("НЕ присутсвуют все три поля")
                logging.error(f'НЕ присутсвуют все три поля {exc} в строке {line}')
            else:
                logging.error(f'поле возраст НЕ является числом от 10 до 99 {exc} в строке {line}')
        except NotNameError:
            logging.error(f'Ошибка в имени в строке {line}')
        except NotEmailError:
            logging.error(f'Поле е-мейл НЕ содержит @ и .в строке {line}')
    # TODO После цикла надо будет закрывать файлы