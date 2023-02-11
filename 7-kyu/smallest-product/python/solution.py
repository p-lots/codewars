from functools import reduce
from operator import mul

def smallest_product(a):
    return min(reduce(mul, subarr) for subarr in a)
