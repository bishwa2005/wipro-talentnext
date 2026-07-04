import re


def is_octal_string(s):
    return bool(re.fullmatch(r"[0-7]+", s))


def filter_octal_strings(strings):
    return [s for s in strings if is_octal_string(s)]


if __name__ == "__main__":
    strings = ['789', '123', '004']
    result = [is_octal_string(s) for s in strings]
    print("Input:", strings)
    print("Octal valid:", result)
    print("Octal-only strings:", filter_octal_strings(strings))
