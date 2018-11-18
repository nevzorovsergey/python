# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный
# случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

# Судя по документации uniform не включает правую границу
array = [random.uniform(0, 50) for i in range(10)]

def merge_sort(array):
    if len(array) > 1:

        lefthalf = array[:len(array)//2]
        righthalf = array[len(array)//2:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = j = k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                array[k] = lefthalf[i]
                i += 1
            else:
                array[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            array[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            array[k] = righthalf[j]
            j += 1
            k += 1

print('Исходный массив ', array)
merge_sort(array)
print('Отсортированный ', array)