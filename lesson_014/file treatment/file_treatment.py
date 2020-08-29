# -*- coding: utf-8 -*-
from bowling import get_score

result_file = open('tournament_result.txt', 'a', encoding='utf8')


def treatment():
    # with open(file_name, 'r', encoding='utf8') as file:
    file = open('tournament.txt', 'r', encoding='utf8')
    for line in file:
        if '### Tour' in line:
            print('\n', line, file=result_file)
        elif len(line) > 20:
            name, res = line.split('\t')
            name = str(name)
            res = str(res)
            try:
                score = []
                score.append(get_score(result=res))
                print(name, res, score, file=result_file)
            except Exception as exc:
                print(line, exc, file=result_file)
        elif 'winner is .........' in line:
            print(line[:-10], file=result_file)
            # try:
            #     print(line[:-10], max(score), file=result_file)
            # except ValueError as val:
            #     print(line[:-10], name, res, score, file=result_file)

            # Это скорее всего происходит из-за того, что вы используете в параметре изменяемый объект
            # Создавайте словарь внутри функции с 0, не надо передавать параметром его
            # А результат надо просто возвращать из фнукции и уже тут сохранять где-то
    file.close()


treatment()

# ### Tour 1  У вас всего 3 типа строк. 1) Начало
# Антон	1/6/1/--327-18812382   2) результаты
# Елена	3532X332/3/62--62X
# Роман	725518X--8/--543152
# Татьяна	8/--35-47/371/518-4/
# Ринат	4-3/7/3/8/X711627-5
# winner is .........   3) конец тура
#  Условиями надо все строки обрабатывать по-своему
# Находите начало - обновляете словарь или список
# Находите результаты - считаете их и добавляете в словарь/список
# Находите конец тура - подсчитываете итоги
# Можно сразу после каждой строки - писать результат в итоговый файл
