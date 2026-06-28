numbers = {10, 20, 30, 40, 50}

print("Original Set:", numbers)

item = int(input("Enter item to remove: "))

if item in numbers:
    numbers.remove(item)
    print("Updated Set:", numbers)
else:
    print("Item not found.")