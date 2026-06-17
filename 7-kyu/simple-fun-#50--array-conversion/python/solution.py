from itertools import islice
from functools import reduce
from operator import mul

def array_conversion(arr, iteration=1):
    if len(arr) == 1:
        return arr[0]
    if iteration % 2 == 1:
        next_arr = [sum(islice(arr, idx, idx + 2)) for idx in range(0, len(arr), 2)]
        return array_conversion(next_arr, iteration + 1)
    else:
        next_arr = [reduce(mul, islice(arr, idx, idx + 2), 1) for idx in range(0, len(arr), 2)]
        return array_conversion(next_arr, iteration + 1)