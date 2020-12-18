from functools import reduce
from operator import mul

def factorial(n):
    if n < 0:
        return None
    elif n <= 1:
        return 1
    return reduce(mul, range(1, n + 1))