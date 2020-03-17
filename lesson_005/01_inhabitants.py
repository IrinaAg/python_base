# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

from lesson_005.room_1 import folks as r1
from lesson_005.room_2 import folks
# TODO дописывать здесь lesson_005 не обязательно
# TODO попробуйте выбрать эту папку слева, нажать правой кнопкой мыши и выбрать mark directory as - source root
print('В комнате room_1 живут:', r1[0], r1[1])  # TODO А тут можно просто использовать join
print('В комнате room_2 живут:', folks[0])