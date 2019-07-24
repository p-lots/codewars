from functools import reduce
from operator import mul

def factorial(n):
    return reduce(mul, [number for number in range(2, n + 1)], 1)