filename = input("Enter file name: ")

file = open(filename, "r")

lines = []

for line in file:
    lines.append(line.strip())

file.close()

print(lines)