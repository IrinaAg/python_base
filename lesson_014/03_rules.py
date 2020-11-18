# -*- coding: utf-8 -*-
import argparse
from file_treatment import treatment, treatment_woldwide

# Прибежал менеджер и сказал что нужно срочно изменить правила подсчета очков в игре.
# "Выходим на внешний рынок, а там правила игры другие!" - сказал он.
#
# Правила подсчета очков изменяются так:
#
# Если во фрейме страйк, сумма очков за этот фрейм будет равна количеству сбитых кеглей в этом фрейме (10 кеглей)
# плюс количество фактически сбитых кеглей за два следующих броска шара (в одном или двух фреймах,
# в зависимости от того, был ли страйк в следующем броске).
# Например: первый бросок шара после страйка - тоже страйк, то +10 (сбил 10 кеглей)
# и второй бросок шара - сбил 2 кегли (не страйк, не важно как закончится этот фрейм - считаем кегли) - то еще +2.
#
# Если во фрейме сбит спэр, то сумма очков будет равна количеству сбитых кеглей в этом фрейме (10 кеглей)
# плюс количество фактически сбитых кеглей за первый бросок шара в следующем фрейме.
#
# Если фрейм остался открытым, то сумма очков будет равна количеству сбитых кеглей в этом фрейме.
#
# Страйк и спэр в последнем фрейме - по 10 очков.
#
# То есть для игры «Х4/34» сумма очков равна 10+10 + 10+3 + 3+4 = 40,
# а для игры «ХXX347/21» - 10+20 + 10+13 + 10+7 + 3+4 + 10+2 + 3 = 92

# Необходимые изменения сделать во всех модулях. Тесты - дополнить.

# "И да, старые правила должны остаться! для внутреннего рынка..." - уточнил менеджер напоследок.


def to_command_line():
    parser = argparse.ArgumentParser(description="Формирования файла с результатами турнира")
    parser.add_argument('input_file', type=str)
    parser.add_argument('output_file', type=str)
    args = parser.parse_args('tournament.txt tour_test.txt'.split())

    question = input("По каким правилам подсчитывать очки: упрощенным - выбрать 1 "
                     "или международным - выбрать любое другое значение?")

    if question == '1':
        treatment(args.input_file, args.output_file)
    else:
        treatment_woldwide(args.input_file, args.output_file)


if __name__ == '__main__':
    to_command_line()

# с подсчётом есть проблемы
# Антон 1/6/1/--327-18812382
#  Результат: Сумма одного фрейма больше 9 очков
# Елена 3532X332/3/62--62X
#  Результат: 11  Результат должен быть 105, а не 11
# Роман 725518X--8/--543152
#  Результат: Сумма одного фрейма больше 9 очков
# Татьяна 8/--35-47/371/518-4/
#  Результат: 11
# Ринат 4-3/7/3/8/X711627-5
#  Результат: 113
# Ринат 4-3/7/3/8/X711627-5
#  Результат: 119
# winner is  Ринат

# пример правильных расчётов
# ### Tour 1
# Антон	1/6/1/--327-18812382     Недопустимая комбинация фрейма - «82»
# Елена	3532X332/3/62--62X       90
# Роман	725518X--8/--543152      Недопустимая комбинация фрейма - «55»
# Татьяна	8/--35-47/371/518-4/ Недопустимая комбинация фрейма - «37»
# Ринат	4-3/7/3/8/X711627-5      119
# winner is Ринат

# ### Tour 2
# Татьяна	42X--3/4/2-8271171/  Недопустимая комбинация фрейма - «82»
# Роман	811/X--3/XX171/43        127
# Ринат	-263X815/5/27-----6      81
# Алексей	--8-X3/4/1/-12651X   88
# Павел	3-6/5/9/5---1/--5-52     79
# winner is Роман