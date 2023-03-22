# week03_prime_number v1.1
#numberstart = int(input("input number to start : "))
#numberend = int(input("input number to end : "))
#count = 0
numbers = input("Enter starting number and ending number : ").split()
numberstart = int(numbers[0])
numberend = int(numbers[1])
for k in range(numberstart, numberend+1):
    is_prime = True
    if k < 2:
        is_prime = False
    else:
        for i in range(2, k): # -2 loop
            if k % i == 0:
                is_prime = False
                break #If not prime number, exit the loop as soon as the firstdivisor is found
    #if is_prime == True:
    if is_prime:
        print(f"{k}", end=' ')
    else:
        continue