# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий,
# чья прибыль ниже среднего.

from collections import namedtuple

QUARTALS = 4
number = int(input('Введите количество предприятий '))

firma = namedtuple('firma', 'name, profits, annular')
allfirms = []
total = 0
for i in range(number):
    allfirms.append(firma(input('Введите название '), [], 0))
    summ = 0
    for q in range(QUARTALS):
        profit = int(input(f'Ввведите прибыть за {q} квартал: '))
        summ += profit
        allfirms[i].profits.append(profit)
        allfirms[i] = allfirms[i]._replace(annular=summ)
    total += summ

avrg = total / number
print('Средняя прибыль за год: ', avrg)

print('Прибыль выше среднего: ')
for i in range(number):
    if allfirms[i].annular > avrg:
        print(allfirms[i].name)

print('Прибыль ниже среднего: ')
for i in range(number):
    if allfirms[i].annular < avrg:
        print(allfirms[i].name)
