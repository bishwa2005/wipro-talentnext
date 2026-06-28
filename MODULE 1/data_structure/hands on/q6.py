import math

def is_prime(num):
    if num <= 1:
        print(f"{num} is not a prime number.")
        return

    prime = True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
