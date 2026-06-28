numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)

index = int(input("Enter index to remove: "))

if index >= 0 and index < len(numbers):
    numbers.pop(index)
    print("Updated List:", numbers)
else:
    print("Invalid index")