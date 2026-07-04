import string


if __name__ == "__main__":
    alphabet_dict = {letter: idx + 1 for idx, letter in enumerate(string.ascii_lowercase)}

    print("Alphabet dictionary:", alphabet_dict)
