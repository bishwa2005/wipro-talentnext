filename = input("Enter file name: ")

file = open(filename, "r")

lines = file.readlines()

# Find meeting time
count = len(lines)

if count <= 12:
    print("Meeting time:", count, "AM")
else:
    print("Meeting time:", count - 12, "PM")

# Count word frequency
words = {}

for line in lines:
    line = line.replace(",", "")
    line = line.replace(".", "")
    line = line.replace('"', "")

    for word in line.split():
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

# Find the most frequent word
place = ""
maximum = 0

for word in words:
    if words[word] > maximum:
        maximum = words[word]
        place = word

print("Meeting place:", place, "Street")

file.close()