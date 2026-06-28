text = input("Enter a string: ")
n = int(input("Enter n: "))

last = text[-n:]

result = ""

for i in range(n):
    result = result + last

print(result)