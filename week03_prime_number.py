# week03_prime_number v0.6
number = int(input("input number : "))
#count = 0
is_prime = True

if number < 2:
    is_prime = False
else:
    for i in range(2, number): # -2 loop
        if number % i == 0:
            is_prime = False
            break #If not prime number, exit the loop as soon as the firstdivisor is found
        print(i, end=' ')

#if is_prime == True:
if is_prime:
    print(f"{number} is prime number!")
else:
    print(f"{number} is not prime number.")