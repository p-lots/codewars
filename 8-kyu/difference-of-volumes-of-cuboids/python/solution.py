from functools import reduce
from operator import mul

def find_difference(a, b):
    return abs(reduce(mul, a, 1) - reduce(mul, b, 1))