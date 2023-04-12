# week04_prime_number v2.0
#numberstart = int(input("input number to start : "))
#numberend = int(input("input number to end : "))
#count = 0
#numbers = input("Enter starting number and ending number : ").split()
#numberstart = int(numbers[0])
#numberend = int(numbers[1])

def is_prime(n) -> bool:
    """
    check prime number
    :param n:
    :return: True (if number is prime number) / False (if number is not a prime number)
    """
    if k < 2:
        return False
    else:
        for i in range(2, k): # -2 loop
            if k % i == 0:
                return False
    return True

numberstart, numberend = map(int, input("Enter starting number and ending number : ").split())
# for k in range(numberstart, numberend+1):
#     if is_prime(k):
#         print(k, end=" ")
#     is_prime = True
#     if k < 2:
#         return False
#     else:
#         for i in range(2, k): # -2 loop
#             if k % i == 0:
#                 return False
#     return True
    #if is_prime == True:
for k in range(numberstart, numberend+1):
    if is_prime(k):
        print(f"{k}", end=' ')
    else:
        continue