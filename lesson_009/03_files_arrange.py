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


class Extract:

    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.time_name = []

    def extract(self):
        for dirpath, dirnames, filenames in os.walk(folder_path):
            # print('{dirpath:-^40}'.format(dirpath=dirpath))
            for file in filenames:
                self.time_file = os.path.join(dirpath, file)
                self.name = os.path.getmtime(self.time_file)
                self.time_name = time.gmtime(self.name)
                # print(self.time_name[])
                # print('{file}||{time_name}'.format(file=file, time_name=time_name))
                # TODO Проблема с одним файлом заключается в том, что проходите вы по всем файлам
                # TODO А далее вызываете метод create и replication отдельно, вне цикла.
                # TODO Вот они и срабатывают по разу.

    def create(self):
        print(self.time_name)
        self.folder_name = '{tm_year}/{tm_mon}'.format(tm_year=self.time_name.tm_year, tm_mon=self.time_name.tm_mon)
        if len(self.folder_name) <= 6:
            self.folder_name = self.folder_name.replace('/', '/0')
        self.new_path = os.path.join(path, self.folder_name)

        if not os.path.exists(self.new_path):
            os.makedirs(self.new_path)  # TODO Тут можно использовать параметр exist_ok=True вместо проверки
            # TODO на наличие папки

    def replication(self):
        print(self.time_file)  # TODO обратите внимание, что в этой переменной уже icons\status\weather-storm.png
        old_image_path = os.path.join(folder_path, self.time_file)
        new_image_path = os.path.join(self.new_path)

        print(old_image_path, new_image_path)  # TODO И новый путь странно формируется icons_by_year\2018/03
        # TODO Вероятно у вас другая ОС, в этом случае путь нужно нормализовать при помощи os.path.normpath
        print(os.path.normpath(self.new_path))
        shutil.copy2(old_image_path, new_image_path)


folder_path = 'icons'
path = 'icons_by_year'
# TODO Если закомментировать эти пути, то видно, что в классе вы используете внешние переменные
# TODO Делать этого не нужно, передавайте их в объект класса переменными
time_name = Extract(folder_path)
time_name.extract()
time_name.create()
time_name.replication()

# изначально делала не на классах, все работает, но на классах только один файл перемещает
# TODO
# for dirpath, dirnames, filenames in os.walk(folder_path):
#     # print('{dirpath:-^40}'.format(dirpath=dirpath))
#     for file in filenames:
#         time_file = os.path.join(dirpath, file)
#         name = os.path.getmtime(time_file)
#         created = time.gmtime(name)
#         # print('{file}||{created}'.format(file=file, created=created))
#         folder_name = '{tm_year}/{tm_mon}'.format(tm_year=created.tm_year, tm_mon=created.tm_mon)
#         if len(folder_name) <= 6:
#             folder_name = folder_name.replace('/', '/0')
#         new_path = os.path.join(path, folder_name)
#         if not os.path.exists(new_path):
#             os.makedirs(new_path)
#         old_image_path = os.path.join(folder_path, time_file)
#         new_image_path = os.path.join(new_path)
#         shutil.copy2(old_image_path, new_image_path)


# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Это относится ктолько к чтению файлов в архиве. В случае паттерна "Шаблонный метод" изменяется способ
# получения данных (читаем os.walk() или zip.namelist и т.д.)
# Документация по zipfile: API https://docs.python.org/3/library/zipfile.html
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
