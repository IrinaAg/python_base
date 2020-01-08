# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

first_educational_grant, expenses = 10000, 12000
difference_sum_first_month = expenses - first_educational_grant
month = 0
expenses_percent = 0
while month < 9:
    expenses = expenses * 1.03
    expenses_percent += expenses
    month += 1
difference_sum = difference_sum_first_month + expenses_percent
insufficient_sum = difference_sum - (9 * first_educational_grant)
print('Студенту надо попросить', round(insufficient_sum, 2), 'рублей')
