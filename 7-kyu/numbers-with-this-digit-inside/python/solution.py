from functools import reduce
from operator import mul

def numbers_with_digit_inside(x, d):
    with_digit = [n for n in range(1, x + 1) if str(d) in str(n)]
    total = sum(with_digit)
    product = reduce(mul, with_digit, 1) if with_digit else 0
    return [len(with_digit), total, product]