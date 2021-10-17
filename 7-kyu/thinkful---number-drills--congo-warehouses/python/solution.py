from operator import mul
from functools import reduce

def box_capacity(length, width, height):
    return reduce(mul, [n * 12 // 16 for n in [length, width, height]])
    