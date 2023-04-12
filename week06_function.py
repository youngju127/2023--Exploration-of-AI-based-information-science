# week06_function.py
def my_generator(first =0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step

ranger = my_generator(5,10)
for k in ranger:
    print(k, end=' ')
for k in ranger:
    print(k, end=' ')
