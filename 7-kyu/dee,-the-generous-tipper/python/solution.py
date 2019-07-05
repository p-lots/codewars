from math import ceil

def calc_tip(p, r):
    rounded = ceil(p / 10) if p % 10 > 4 else p // 10
    rounded = rounded + 1 if r == 1 else rounded - 1 if r == 0 else rounded // 2 - 1
    return max(rounded, 0)
