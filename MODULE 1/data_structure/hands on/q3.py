def last_digit(num1, num2):
    # Using modulus 10 extracts the final digit
    return (num1 % 10) == (num2 % 10)

# Examples
print(last_digit(7, 17))   # True
print(last_digit(6, 17))   # False
print(last_digit(3, 113))  # True
