# -*- coding: utf-8 -*-
from bowling import get_score
from woldwide import get_score_woldwide


def treatment(input_file, output_file):
    input_file = open('/Users/agafonova/python_base/lesson_014/tournament.txt', 'r', encoding='utf8')
    output_file = open('/Users/agafonova/python_base/lesson_014/tournament_result.txt', 'a', encoding='utf8')
    for line in input_file:
        if '### Tour' in line:
            score = {}
            print('\n', line, file=output_file)
        elif len(line) > 20:
            name, res = line.split('\t')
            name = str(name)
            res = str(res)
            try:
                score[name] = get_score(result=res)
                print(name, res, 'Результат:', get_score(result=res), file=output_file)
            except Exception as exc:
                print(name, res, 'Результат:', exc, file=output_file)
        elif 'winner is .........' in line:
            try:
                for key in sorted(score.items(), key=lambda para: (para[1], para[0]), reverse=False):
                    print(key)
                print(line[:-10], key[0], file=output_file)
            except ValueError:
                print('Победителя нет', file=output_file)

    input_file.close()


if __name__ == '__main__':
    treatment(input_file='tournament.txt', output_file='tournament_result.txt')


def treatment_woldwide(input_file, output_file):
    # обратите внимание, что параметры у вас никак не используются
    # TODO Параметры надо использовать + нельзя использовать абсолютные пути!
    input_file = open('tournament.txt', 'r', encoding='utf8')
    output_file = open('tournament_result.txt', 'a', encoding='utf8')
    # TODO Пути старайтесь указывать относительно рабочей директории (той, в которой лежит главный запускаемый файл)
    # TODO т.к. здесь у нас проект состоит из нескольких "мини"-проектов, то можно выполнить хитрый приём, явно указав
    # TODO на рабочую директорию.
    # TODO Сделать это можно либо в Run - Edit configurations
    # TODO Либо можно просто выделить нужную папку как source root
    # TODO для этого надо нажать на неё правой кнопкой - mark directory as - source root
    # TODO Либо, если запуск идёт через терминал - нужно в самом терминале отркыть рабочую директорию
    # TODO (путь указанный в терминале - используется как рабочая директория)
    # TODO Сделать это можно 2 способами
    # TODO 1) использовать команду терминала cd (change directory)
    # TODO 2) ПКМ на нужной папке в пайчарме - open in terminal
    # TODO Не забывайте о стиле кода (в этом вам отчасти поможет code/reformat code - или просто ctrl + alt + L)

    for line in input_file:
        if '### Tour' in line:
            score = {}
            print('\n', line, file=output_file)
        elif len(line) > 20:
            name, res = line.split('\t')
            name = str(name)
            res = str(res)
            try:
                score[name] = get_score_woldwide(result=res)
                print(name, res, 'Результат:', get_score_woldwide(result=res), file=output_file)
            except Exception as exc:
                print(name, res, 'Результат:', exc, file=output_file)
        elif 'winner is .........' in line:
            try:
                for key in sorted(score.items(), key=lambda para: (para[1], para[0]), reverse=False):
                    print(key)
                print(line[:-10], key[0], file=output_file)
            except ValueError:
                print('Победителя нет', file=output_file)

    input_file.close()


if __name__ == '__main__':
    treatment_woldwide(input_file='tournament.txt', output_file='tournament_result.txt')
