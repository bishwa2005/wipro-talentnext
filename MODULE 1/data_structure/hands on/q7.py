import math

def print_primes_in_range():
    for i in range(10, 100):
        is_prime = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            print(i, end=" ")
    print()
