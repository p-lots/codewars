def square_digits(num):
    digits = [str(int(digit) ** 2) for digit in str(num)]
    return int(''.join(digits))