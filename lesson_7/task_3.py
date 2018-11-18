# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найти в массиве медиану. Медианой называется элемент ряда, делящий его на две равные
# части: в одной находятся элементы, которые не меньше медианы, в другой – не больше ее.

import random

m = 10
array = [random.randint(0,100) for i in range(2*m+1)]

def find_median(array):
    best  = len(array)
    best_i = len(array) - 1
    for i in range(len(array)):
        n = m = 0;
        for j in range(len(array)):
            if array[j] != array[i]:
                if array[j] > array[i]:
                    n += 1
                else:
                    m += 1
        if n == m:
            return i
        if abs(m - n) < best:
            best = abs(m - n)
            best_i = i

    return best_i


print('Исходный массив ', array)
med = find_median(array)
print('Медиана: ', array[med])

# Для проверки, сделаем тоже самое с сортировкой:
array = sorted(array)
print('Отсортированный ', array)
print('Медиана в отсортированном массиве: ', array[len(array)//2])
