# -*- coding: utf-8 -*-
from bowling import get_score

my_dict = {}
result_file = open('tournament_result.txt', 'r', encoding='utf8')


def treatment():
    # with open(file_name, 'r', encoding='utf8') as file:
    file = open('tournament.txt')
    for line in file:
        tour = line.split('winner is .........')
        tour = str(tour)
        if '### Tour' not in line:
            # проходит только до первой записи "winner is ........." как пойти дальше по файлу
            # print(line.strip())
            # не могу понять(
            # if 'winner is' not in line:
            # if not line.strip():
            #     continue
            my_dict = line.split('\t')
            result = my_dict[1]
            try:
                get_score(result=result, analized_res={})
                # TODO Это скорее всего происходит из-за того, что вы используете в параметре изменяемый объект
                # TODO Создавайте словарь внутри функции с 0, не надо передавать параметром его
                # TODO А результат надо просто возвращать из фнукции и уже тут сохранять где-то
                # очки считаются прибавлением результата всех игроков, надо
                # обнулить результат, но тоже не понимаю где его обнулить
            except ValueError as val:
                print(line, val)
            except Exception as exc:
                print(line, exc)
        # else:
        #     return


treatment()

#
# with open('tournament_result.txt', 'r', encoding='utf8') as ff:
#     for line in ff:
#         try:
#             treatment()
#             get_score(result=my_dict[1], analized_res={})
#             # print(my_dict[1], file=result_file)
#         except ValueError as val:
#             print(line, val)
#         except Exception as exc:
#             print(line, exc)
#
#     result_file.close()
# ### Tour 1  TODO У вас всего 3 типа строк. 1) Начало
# Антон	1/6/1/--327-18812382  TODO 2) результаты
# Елена	3532X332/3/62--62X
# Роман	725518X--8/--543152
# Татьяна	8/--35-47/371/518-4/
# Ринат	4-3/7/3/8/X711627-5
# winner is .........  TODO 3) конец тура
# TODO Условиями надо все строки обрабатывать по-своему
# TODO Находите начало - обновляете словарь или список
# TODO Находите результаты - считаете их и добавляете в словарь/список
# TODO Находите конец тура - подсчитываете итоги
# TODO Можно сразу после каждой строки - писать результат в итоговый файл