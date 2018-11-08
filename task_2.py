# 2. Написать два алгоритма нахождения i-го по счёту простого числа. Первый - использовать алгоритм решето Эратосфена.
# Второй - без использования "решета".
# Проанализировать скорость и сложность алгоритмов.

import cProfile

def sieve(n):
    si = [i for i in range(n*n)]
    si[1] = 0
    for i in range(2, n*n):
        if si[i] != 0:
            j = i + i
            while j < n*n:
                #print(j)
                si[j] = 0
                j +=i

    primes = [i for i in si if i != 0]
    return primes[n - 1]

# cProfile.run('sieve(10)')   1    0.003    0.003    0.003    0.003 task_2.py:3(sieve)
# cProfile.run('sieve(100)')  1    0.021    0.021    0.024    0.024 task_2.py:3(sieve)
# cProfile.run('sieve(1000)') 1    1.743    1.743    2.001    2.001 task_2.py:3(sieve)

# task_2.sieve(10)   10 loops, best of 5: 56.1 usec per loop
# task_2.sieve(100)  10 loops, best of 5: 10.5 msec per loop
# task_2.sieve(1000) 10 loops, best of 5: 1.79 sec per loop

def prime(i, primes):
    for prime in primes:
        if not (i == prime or i % prime):
            return False
    primes.append(i)
    return i

def historic(n):
    primes = []
    i, p = 2, 0
    while True:
        if prime(i, primes):
            p += 1
            if p == n:
                return primes[len(primes)-1]
        i += 1

# cProfile.run('historic(10)')    1    0.000    0.000    0.000    0.000 task_2.py:28(historic)
# cProfile.run('historic(1000)')  1    0.004    0.004    0.101    0.101 task_2.py:28(historic)
# cProfile.run('historic(10000)') 1    0.085    0.085   18.385   18.385 task_2.py:28(historic)

# task_2.historic(10)   10 loops, best of 5: 47.3 usec per loop
# task_2.historic(100)  10 loops, best of 5: 1.2 msec per loop
# task_2.historic(1000) 10 loops, best of 5: 112 msec per loop

#print(sieve(1000))
#print(historic(1000))

#  Вывод: второй алгоритм получился почти в 10 раз быстрее