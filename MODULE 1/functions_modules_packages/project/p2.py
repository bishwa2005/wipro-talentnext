def ispalindrome(name):
    if name == name[::-1]:
        print("Yes it is a palindrome.")
    else:
        print("No it is not a palindrome.")


def count_the_vowels(name):
    vowels = "aeiouAEIOU"
    count = 0

    for ch in name:
        if ch in vowels:
            count += 1

    print("No of vowels:", count)


def frequency_of_letters(name):
    visited = []

    print("Frequency of letters:", end=" ")

    for ch in name:
        if ch not in visited:
            count = 0

            for letter in name:
                if ch == letter:
                    count += 1

            print(ch, "-", count, end=", ", sep="")
            visited.append(ch)

    print()