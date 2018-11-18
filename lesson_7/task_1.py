# 1. Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив, заданный случайными числами
# на промежутке [-100; 100). Вывести на экран исходный и отсортированный массивы.

import random

array = [random.randrange(-100,100) for i in range(10)]

def bubble_sort(array):
    n = 1
    changed = True # Если что-то поменяли, то идем дальше, иначе если за цикл так ничего и не поменяли, то массив уже отсортирован
    while n < len(array) and changed:
        changed = False
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                changed = True

        n += 1
 #       print(array)


print('Исходный массив ', array)
bubble_sort(array)
print('Отсортированный ', array)
