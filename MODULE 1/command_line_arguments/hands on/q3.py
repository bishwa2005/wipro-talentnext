import sys

def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


total = 0

for i in range(1, 11):
    number = int(sys.argv[i])

    if is_prime(number):
        total += number

print("Sum of prime numbers:", total)