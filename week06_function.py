# week06_function.py
import time
# def my_generator(first =0, last=10, step=1):
#     number = first
#     while number < last:
#         yield number
#         number += step
#
# ranger = my_generator(5,10)
# for k in ranger:
#     print(k, end=' ')
# for k in ranger:
#     print(k, end=' ')

def factorial(n):

    s = time.time()
    result = 1
    for k in range(1, n+1):
        result *= k
    e = time.time()
    print(f'total time is {e-s} second')
    return result
def power(b, e):
    s = time.time()
    n = b**e
    t = time.time()
    print(f'total time is {t-s}second')

print(factorial(1000))
