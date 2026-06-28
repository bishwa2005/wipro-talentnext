filename = input("Enter file name: ")

search = input("Enter word to search: ")

file = open(filename, "r")

count = 0

for line in file:
    words = line.split()

    for word in words:
        word = word.strip(",.!?")

        if word == search:
            count += 1

file.close()

print("Frequency:", count)