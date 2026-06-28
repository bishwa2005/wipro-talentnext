sentence = input("Enter a sentence: ")

words = sentence.split()

count = 0

for word in words:
    cleaned_word = word.strip(".,!?")
    if cleaned_word == "Alex":
        count += 1

print("Number of occurrences:", count)