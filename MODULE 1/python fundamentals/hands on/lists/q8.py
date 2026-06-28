numbers = [10, 20, 30, 20, 40, 50]

print("Original List:", numbers)

element = int(input("Enter element to remove: "))

if element in numbers:
    numbers.remove(element)
    print("Updated List:", numbers)
else:
    print("Element not found")