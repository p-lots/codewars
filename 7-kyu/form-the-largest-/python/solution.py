from functools import reduce

def max_number(n):
    return reduce(lambda acc, dig: acc * 10 + dig, sorted([int(digit) for digit in str(n)], reverse=True))