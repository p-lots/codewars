from functools import reduce
from operator import mul

def sum_or_product(array, n):
    array = sorted(array)
    product = reduce(mul, array[:n], 1)
    total = sum(array[-n:])
    return 'sum' if total > product else 'product' if product > total else 'same'
