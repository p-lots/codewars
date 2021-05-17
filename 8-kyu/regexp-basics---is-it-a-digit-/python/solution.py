import string

def is_digit(n):
    return all(ch in string.digits for ch in n) and len(n) == 1 if n else False