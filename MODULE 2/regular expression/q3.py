import re


def normalize_sentence(sentence):
    words = re.split(r"[\W_]+", sentence)
    return ' '.join(word for word in words if word)


if __name__ == "__main__":
    sentence = "A, very very; irregular_sentence"
    normalized = normalize_sentence(sentence)
    print("Original:", sentence)
    print("Normalized:", normalized)
