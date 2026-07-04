import re


def same_start_end(words):
    return [word for word in words if len(word) > 0 and word[0].lower() == word[-1].lower()]


if __name__ == "__main__":
    words = ['civic', 'trust', 'widows', 'maximum', 'museums', 'aa', 'as']
    print("Words:", words)
    print("Same start and end:", same_start_end(words))
