from math import log2, ceil

def score(n):
    if n == 0 or n == 1:
        return n
    return 2 ** ceil(log2(n)) - 1
