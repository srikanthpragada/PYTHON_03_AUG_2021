# Module containing string related functions

def count_upper(st):
    c = 0
    for ch in st:
        if ch.isupper():
            c += 1

    return c


def has_digit(st):
    for ch in st:
        if ch.isdigit():
            return True

    return False


if __name__ == '__main__':
    print("String Functions Ver 1.0")
    print(has_digit("abc"), has_digit("adf34343"))