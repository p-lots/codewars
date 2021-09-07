from functools import reduce
from operator import mul

def math_engine(arr):
    if arr == None:
        return 0
    elif len(arr) == 0:
        return 1
    negatives = [n for n in arr if n < 0]
    positives = [n for n in arr if n >= 0]
    if len(negatives) == 0 and len(positives) > 0:
        return reduce(mul, positives, 1)
    elif len(positives) == 0 and len(negatives) > 0:
        return sum(negatives) + 1
    elif len(negatives) == 0 and len(positives) == 0:
        return 0
    return reduce(mul, positives, 1) + sum(negatives)
