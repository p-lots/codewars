from functools import reduce

def min_value(digits):
    dig_set = sorted(set(digits))
    return reduce(lambda acc, n: acc * 10 + n, dig_set)