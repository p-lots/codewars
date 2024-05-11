from functools import reduce
from operator import mul

def product_array(numbers):
    prod = reduce(mul, numbers, 1)
    return [prod / number for number in numbers]
