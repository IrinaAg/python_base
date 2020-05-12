# -*- coding: utf-8 -*-

import os, time, shutil


# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.


# class Extract:
#
#     def __init__(self, folder_path):
#         self.folder_path = folder_path
#         self.time_file1 = []
#         self.time_name1 = []
#         self.new_path = []
#
#     def extract(self):
#         # self.time_file1 = []  # Проблема с атрибутами
#         # Если они используются в нескольких методах - то нужно сперва их задать в init, а потом использовать
#         # Если атрибут используется только в одном методе - можно сделать его обычной переменной
#         # self.time_name1 = []
#         for dirpath, dirnames, filenames in os.walk(folder_path):
#             for file in filenames:
#                 time_file = os.path.join(dirpath, file)
#                 self.time_file1.append(time_file)
#                 name = os.path.getmtime(time_file)
#                 time_name = time.gmtime(name)
#                 self.time_name1.append(time_name)
#
#     def create(self):
#         for time_name in self.time_name1:
#             self.folder_name = '{tm_year}/{tm_mon}'.format(tm_year=time_name.tm_year,
#                                                            tm_mon=time_name.tm_mon)
#             if len(self.folder_name) <= 6:
#                 self.folder_name = self.folder_name.replace('/', '/0')
#             new_path = os.path.join(path, self.folder_name)
#             self.new_path.append(new_path)
#             os.makedirs(new_path, exist_ok=True)
#
#     def replication(self):
#         for time_file in self.time_file1:
#             old_image_path = os.path.join(time_file)
#             for new_path in self.new_path:
#                 # Мне кажется тут разделение по методам запутало вас
#                 # Попробуйте в одном цикле идти по файлам
#                 # брать полный путь до текущего файла, составлять новый путь из новой директории + год + месяц
#                 # и сразу же переносить.
#                 # Так то шаги алгоритма верные, но мне кажется создаётся путанница из-за
#                 # лишнего сбора и хранения данных
#                 new_image_path = os.path.join(os.path.normpath(new_path))
#                 shutil.copy2(old_image_path, new_image_path)


# folder_path = 'icons'
# path = 'icons_by_year'
# time_name = Extract(folder_path)
# time_name.extract()
# time_name.create()
# time_name.replication()


class Extract:  # если один метод все работает

    def __init__(self, folder_path):
        self.folder_path = folder_path

    def extract(self):
        for dirpath, dirnames, filenames in os.walk(folder_path):
            for file in filenames:
                time_file = os.path.join(dirpath, file)
                name = os.path.getmtime(time_file)
                created = time.gmtime(name)
                folder_name = '{tm_year}/{tm_mon}'.format(tm_year=created.tm_year, tm_mon=created.tm_mon)
                if len(folder_name) <= 6:
                    folder_name = folder_name.replace('/', '/0')
                new_path = os.path.join(path, folder_name)
                os.makedirs(new_path, exist_ok=True)
                old_image_path = os.path.join(time_file)
                new_image_path = os.path.join(new_path)
                shutil.copy2(old_image_path, new_image_path)


folder_path = 'icons'
path = 'icons_by_year'
time_name = Extract(folder_path)
time_name.extract()



# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Это относится ктолько к чтению файлов в архиве. В случае паттерна "Шаблонный метод" изменяется способ
# получения данных (читаем os.walk() или zip.namelist и т.д.)
# Документация по zipfile: API https://docs.python.org/3/library/zipfile.html
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
