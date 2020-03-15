# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from lesson_005.district.central_street.house1.room1 import folks as cent_st_h1_r1
from lesson_005.district.central_street.house1.room2 import folks as cent_st_h1_r2
from lesson_005.district.central_street.house2.room1 import folks as cent_st_h2_r1
from lesson_005.district.central_street.house2.room2 import folks as cent_st_h2_r2
from lesson_005.district.soviet_street.house1.room1 import folks as sov_st_h1_r1
from lesson_005.district.soviet_street.house1.room2 import folks as sov_st_h1_r2
from lesson_005.district.soviet_street.house2.room1 import folks as sov_st_h2_r1
from lesson_005.district.soviet_street.house2.room2 import folks as sov_st_h2_r2

district_residents = cent_st_h1_r1 + cent_st_h1_r2 + cent_st_h2_r1 + cent_st_h2_r2 + sov_st_h1_r1 + sov_st_h1_r2 + \
                     sov_st_h2_r1 + sov_st_h2_r2

print(', '.join(district_residents))

