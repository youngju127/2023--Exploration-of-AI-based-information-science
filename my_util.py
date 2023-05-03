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