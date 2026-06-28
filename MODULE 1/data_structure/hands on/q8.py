def find_sum(num):
    digit_sum = 0
    original_num = num
    
    while num > 0:
        digit_sum += num % 10  # Extract last digit
        num //= 10             # Remove last digit (integer division)
        
    print(f"Sum of digits of {original_num} is: {digit_sum}")
