# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.

from collections import deque

allhex = '0123456789ABCDEF'

def hex_add(n1,n2):
    next = 0
    result = deque()
    while len(n1) > 0 or len(n2) > 0:
        simb1 = n1.pop() if len(n1) > 0 else '0'
        simb2 = n2.pop() if len(n2) > 0 else '0'

        num1 = allhex.index(simb1)
        num2 = allhex.index(simb2)
        summ = num1 + num2 + next

        result.appendleft(allhex[summ % 16])
        next = summ // 16

    if next > 0:
        result.appendleft(allhex[next])

    return result

def hex_mult(n1,n2):
    len1 = len(n1)
    len2 = len(n2)
    result = deque()
    for i in range(len1):
        next = 0
        simb1 = n1[len1-i-1]
        num1 = allhex.index(simb1)
        tempresult = deque('0'*i)
        for j in range(len2):
            simb2 = n2[len2-j-1]
            num2 = allhex.index(simb2)
            mult = num1 * num2 + next

            tempresult.appendleft(allhex[mult % 16])
            next = mult // 16
        if next > 0:
            tempresult.appendleft(allhex[next])

        result = hex_add(tempresult, result)

    return result

n1 = input('Введите первое шестнадцатеричное число: ')
n2 = input('Введите второе шестнадцатеричное число: ')

print('Сумма: ', hex_add(deque(n1), deque(n2)))
print('Произведение: ', hex_mult(deque(n1), deque(n2)))
