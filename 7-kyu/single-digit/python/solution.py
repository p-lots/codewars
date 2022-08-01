def single_digit(n):
    while n >= 10:
        n = sum(int(digit) for digit in f'{n:b}')
    return n
