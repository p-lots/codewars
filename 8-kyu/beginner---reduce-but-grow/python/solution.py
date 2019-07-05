from functools import reduce
import operator

def grow(arr):
    return reduce(operator.__mul__, arr, 1)