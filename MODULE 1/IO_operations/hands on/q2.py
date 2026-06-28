filename = input("Enter file name: ")
n = int(input("Enter number of lines: "))

file = open(filename, "r")

for i in range(n):
    line = file.readline()

    if line == "":
        break

    print(line, end="")

file.close()