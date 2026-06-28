filename = input("Enter file name: ")

file = open(filename, "r")

longest = ""

for line in file:
    words = line.split()

    for word in words:
        word = word.strip(",.!?")

        if len(word) > len(longest):
            longest = word

file.close()

print("Longest word:", longest)