sentence = input("Enter a sentence: ")

count = 0

words = sentence.split()

for word in words:
    word = word.strip(".,!?")

    if word == "Alex":
        count += 1

print("Number of times Alex appears:", count)