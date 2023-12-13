from functools import reduce
from operator import mul

def persistence(n):
    if n < 10:
        return 0
    ret = 0
    while len(str(n)) > 1:
        n = reduce(mul, map(int, str(n)))
        ret += 1
    return ret