# -*- coding: utf-8 -*-
import argparse
import os
from PIL import Image, ImageDraw, ImageFont, ImageColor


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru

# def make_ticket(fio, from_, to, date):
#     pass

# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля argparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.


# class TicketMaker:
#
#     def __init__(self, template=None, font_path=None):
#         self.template = "images/ticket_template.png" if template is None else template
#         if font_path is None:
#             self.font_path = "python_snippets/fonts/Bressay Display.ttf"
#         else:
#             self.font_path = font_path
#
#     def make_ticket(self, save_to=None):
#         im = Image.open(self.template)
#         draw = ImageDraw.Draw(im)
#         font = ImageFont.truetype(self.font_path, size=16)
#
#         y = im.size[1] - 225 - (10 + font.size) * 2
#         fio = f"ИВАНОВ И.И."
#         draw.text((50, y), fio, font=font, fill=ImageColor.colormap['black'])
#
#         y = im.size[1] - 190 - font.size
#         from_ = f"ЗЕМЛЯ"
#         draw.text((50, y), from_, font=font, fill=ImageColor.colormap['black'])
#
#         y = im.size[1] - 125 - font.size
#         to = f"ЛУНА"
#         draw.text((50, y), to, font=font, fill=ImageColor.colormap['black'])
#
#         y = im.size[1] - 125 - font.size
#         date = f"09.12"
#         draw.text((290, y), date, font=font, fill=ImageColor.colormap['black'])
#
#         # im.show()
#         save_to = save_to if save_to else 'ticket_image.png'
#         dir_path = "/Users/agafonova/python_base/lesson_013/test"
#         os.makedirs(dir_path, exist_ok=True)
#         file_path = os.path.join(dir_path, save_to)
#         im.save(file_path)
#         print(f'Ticket saved az {save_to}')
#
#
# if __name__ == '__main__':
#     maker = TicketMaker()
#     maker.make_ticket()

# Усложненная часть с argparse


def make_ticket():
    # TODO 1) Пути надо указать относительно директории lesson_013
    im = Image.open("images/ticket_template.png")  # TODO Примерно так
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("/Users/agafonova/python_base/lesson_013/python_snippets/fonts/Bressay Display.ttf",
                              size=16)
    # TODO Аргпарсер должен быть вне функции
    # TODO Это отдельный элемент программы, который может быть одним из вариантов запуска вашей функции
    # TODO Его можно выделить или в отдельную функцию, или просто записать в if __name__ == '__main__'
    parser = argparse.ArgumentParser(description='Заполнение билета')
    parser.add_argument('fio', type=str, help='фамилия')
    parser.add_argument('from_', type=str, help='откуда летим')
    parser.add_argument('to', type=str, help='куда летим')
    parser.add_argument('date', type=str, help='когда летим')
    args = parser.parse_args()
    # TODO А уже потом передавать все вот эти аргументы в функцию, как при обычном вызове
    y = im.size[1] - 225 - (10 + font.size) * 2
    draw.text((50, y), args.fio, font=font, fill=ImageColor.colormap['black'])

    y = im.size[1] - 190 - font.size
    draw.text((50, y), args.from_, font=font, fill=ImageColor.colormap['black'])

    y = im.size[1] - 125 - font.size
    draw.text((50, y), args.to, font=font, fill=ImageColor.colormap['black'])

    y = im.size[1] - 125 - font.size
    draw.text((290, y), args.date, font=font, fill=ImageColor.colormap['black'])
    im.show()
    parser.add_argument('-s', '--save_to', help='путь для сохранения заполненнего билета')
    save_to = 'ticket_image.png'
    dir_path = "/Users/agafonova/python_base/lesson_013/test"  # TODO И тут путь поправить
    os.makedirs(dir_path, exist_ok=True)
    file_path = os.path.join(dir_path, save_to)
    im.save(file_path)


if __name__ == '__main__':
    make_ticket()
