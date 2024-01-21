from itertools import pairwise
from math import copysign

def catch_sign_change(lst):
    sign = lambda n: copysign(1, n)
    return sum(sign(prev) != sign(next) for prev, next in pairwise(lst))