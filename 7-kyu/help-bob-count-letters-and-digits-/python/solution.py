def count_letters_and_digits(s):
    return sum(1 for ch in s if ch.isalpha() or ch.isdigit())