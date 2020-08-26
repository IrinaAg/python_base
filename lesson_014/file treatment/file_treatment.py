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
        if '### Tour' not in line: #TODO проходит только до первой записи "winner is ........." как пойти дальше по файлу
            # print(line.strip())#TODO не могу понять(
            # if 'winner is' not in line:
                # if not line.strip():
                #     continue
            my_dict = line.split('\t')
            result = my_dict[1]
            try:
                get_score(result=result, analized_res={}) #TODO очки считаются прибавлением результата всех игроков, надо
                #TODO обнулить результат, но тоже не понимаю где его обнулить
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


