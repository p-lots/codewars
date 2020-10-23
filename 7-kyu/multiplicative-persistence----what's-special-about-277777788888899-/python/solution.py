from functools import reduce
from operator import mul

def per(n):
    ret = []
    if n < 10:
        return ret
    while len(str(n)) > 1:
        new_n = int(reduce(mul, map(int, str(n))))
        ret.append(new_n)
        n = new_n
    return ret