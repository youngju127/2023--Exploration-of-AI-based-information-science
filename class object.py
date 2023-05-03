# animal = 'fruitbat'
#
# def change_and_print_global():
#     ''' function'''
#     global animal
#     student = 'woojin'
#     print('inside change_and_print_animal', animal)
#     animal = 'wombat'
#     print('after the change', animal)
#     print(locals())
#     print(change_and_print_global,__name__)
#     print(change_and_print_global,__doc__)
#
# if __name__ == "__main__":
#     print(__name__)
# print('at the top level', animal)
# change_and_print_global()
#
# print(locals())

import my_util
@my_util.time_checker
def factorial_recursion(n):
    '''
    factorial function with recursion
    :param n: more than zero
    :return: n!
    '''
    if n == 1:
        return 1
    else:
        return n * factorial_recursion(n-1)

memo = [None for _ in range(100)]
@my_util.time_checker
def fibonacci_recursion(n):
    '''
    fibo
    :param n: integer value
    :return: fibonacci number
    '''
    if n<=1:
        return n
    if memo[n] != 0:
        return memo[n]
    else:
        memo[n] = fibonacci_recursion(n-1) + fibonacci_recursion(n-2)
        return fibonacci_recursion(n-1)+ fibonacci_recursion(n-2)


if __name__ =="__main__":
    number = int(input())
    print(factorial_recursion(number))
    print(fibonacci_recursion(number))
