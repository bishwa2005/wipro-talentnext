numbers = (10, 20, 30, 40, 50)

element = int(input("Enter the element: "))

if element in numbers:
    index = numbers.index(element)
    print("Index:", index)
else:
    print("Element not found.")