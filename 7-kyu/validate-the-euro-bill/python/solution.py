from string import ascii_uppercase as alphabet

def validate_euro(serial_number):
    digit_total = sum(alphabet.index(ch) + 1 if ch.isalpha() else int(ch) for ch in serial_number)
    return digit_total % 9 == 7
