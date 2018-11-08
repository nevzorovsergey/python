# 1. Проанализировать скорость и сложность одного - трёх любых алгоритмов, разработанных в рамках
# домашнего задания первых трех уроков.

# Написать программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется
# равенство: 1+2+...+n = n(n+1)/2, где n – любое натуральное число.
import cProfile


def v_while(n):
    n_by_circle = 0
    n_by_formula = n*(n+1)/2

    while n > 0:
        n_by_circle += n
        n -= 1

    return n_by_circle == n_by_formula

# n= 100000
# Замер 1
# cProfile.run('v_while(100000)') 1    0.026    0.026    0.026    0.026 task_7.py:9(v_while)
# Замер 2
# cProfile.run('v_while(100000)') 1    0.023    0.023    0.023    0.023 task_7.py:9(v_while)
# Замер 3
# cProfile.run('v_while(100000)') 1    0.024    0.024    0.024    0.024 task_7.py:9(v_while)
# Среднее время 0.024

# n= 1000000
# Замер 1
# cProfile.run('v_while(1000000)') 1    0.246    0.246    0.246    0.246 task_7.py:9(v_while)
# Замер 2
# cProfile.run('v_while(1000000)') 1    0.240    0.240    0.240    0.240 task_7.py:9(v_while)
# Замер 3
# cProfile.run('v_while(1000000)') 1    0.326    0.326    0.326    0.326 task_7.py:9(v_while)
# Среднее время 0.270

# n= 10000000
# Замер 1
# cProfile.run('v_while(10000000)')   1    2.589    2.589    2.589    2.589 task_7.py:9(v_while)
# Замер 2
# cProfile.run('v_while(10000000)')   1    2.634    2.634    2.634    2.634 task_7.py:9(v_while)
# Замер 3
# cProfile.run('v_while(10000000)')   1    2.984    2.984    2.984    2.984 task_7.py:9(v_while)
# Среднее время 2.735

# timeit
# task_1.v_while(100000) 100 loops, best of 5: 25 msec per loop
# task_1.v_while(1000000) 100 loops, best of 5: 263 msec per loop
# task_1.v_while(10000000) 100 loops, best of 5: 2.95 sec per loop


def v_range(n):
    n_by_circle = 0
    n_by_formula = n * (n + 1) // 2

    for i in range(1, n + 1):
        n_by_circle += i

    return n_by_circle == n_by_formula

# n= 100000
# Замер 1
# cProfile.run('v_range(100000)')        1    0.014    0.014    0.014    0.014 task_7.py:46(v_range)
# Замер 2
# cProfile.run('v_range(100000)')        1    0.018    0.018    0.018    0.018 task_7.py:46(v_range)
# Замер 3
# cProfile.run('v_range(100000)')        1    0.014    0.014    0.014    0.014 task_7.py:46(v_range)
# Среднее время 0.015

# n= 1000000
# Замер 1
# cProfile.run('v_range(1000000)')       1    0.172    0.172    0.172    0.172 task_7.py:46(v_range)
# Замер 2
# cProfile.run('v_range(1000000)')       1    0.152    0.152    0.152    0.152 task_7.py:46(v_range)
# Замер 3
# cProfile.run('v_range(1000000)')       1    0.157    0.157    0.157    0.157 task_7.py:46(v_range)
# Среднее время 0.160

# n= 10000000
# Замер 1
# cProfile.run('v_range(10000000)')        1    1.613    1.613    1.613    1.613 task_7.py:46(v_range)
# Замер 2
# cProfile.run('v_range(10000000)')        1    1.658    1.658    1.658    1.658 task_7.py:46(v_range)
# Замер 3
# cProfile.run('v_range(10000000)')        1    1.631    1.631    1.631    1.631 task_7.py:46(v_range)
# Среднее время 1.634


# timeit
# task_1.v_range(100000) 100 loops, best of 5: 23.3 msec per loop
# task_1.v_range(1000000) 100 loops, best of 5: 227 msec per loop
# task_1.v_range(10000000) 100 loops, best of 5: 2.33 sec per loop


#cProfile.run('v_range(10000000)')


# Вывод: Замеры cProfile выявили преимущество через цикл for .. range перед циклом while, почти на 30%,
# что мне показалось странным. Затем замеры через timeit со 100 циклами замера. Видимо timeit замеряет
# более точно, т.к. при данном типе замера существенной разницы не замечено.
# Ассимптотика этих алгоритмов линейная.





