text = input("Enter a string: ")

first = text[:2]

result = ""

for i in range(len(text)):
    result = result + first

print(result)