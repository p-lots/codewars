from operator import mul
from functools import reduce

def product(numbers):
    return reduce(mul, numbers, 1) if numbers else None