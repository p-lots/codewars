from functools import reduce
from operator import mul

def process_data(data):
    return reduce(mul, [first - second for first, second in data], 1)
