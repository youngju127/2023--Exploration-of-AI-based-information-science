# week06_function.py

# def my_generator(first =0, last=10, step=1):
#     number = first
#     while number < last:
#         yield number
#         number += step

# ranger = my_generator(5,10)
# for k in ranger:
#     print(k, end=' ')
# for k in ranger:
#     print(k, end=' ')

# s = time.time()
# t = time.time()
# print(f'total time is {t - s}second')

import time
def time_checker(func): #closure
    def inner(*args):
        s = time.time()
        r = func(*args)
        e = time.time()
        print(f'total time is {e - s}second')
        return r
    return inner
@time_checker
def factorial(n):
    result = 1
    for k in range(1, n+1):
        result *= k
    return result

@time_checker
def power(b, e):
    n = b**e
    return n


print(power(2, 100))

