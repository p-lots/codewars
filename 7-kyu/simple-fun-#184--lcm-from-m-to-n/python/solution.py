from functools import reduce
from math import lcm

def mn_lcm(m, n):
    smaller = min(m, n)
    larger = max(m, n)
    return reduce(lcm, range(smaller, larger + 1))
