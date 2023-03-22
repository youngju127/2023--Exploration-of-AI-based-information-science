# week03_prime_number v0.2
number = int(input("input number : "))
#count = 0
is_prime = True

for i in range(2, number): # -2 loop
    if number % i == 0:
    is_prime = False

if is_prime == 0:
    print(f"{number} is prime number!")
else:
    print(f"{number} is not prime number.")