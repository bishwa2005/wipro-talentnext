filename = input("Enter file name: ")

text = input("Enter text to append: ")

file = open(filename, "a")

file.write(text)
file.write("\n")

file.close()

print("Data appended successfully.")