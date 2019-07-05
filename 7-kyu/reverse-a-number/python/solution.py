from math import floor, log10

def reverse_number(n):
    if n > -10 and n < 10:
        return n
    n_abs = abs(n)
    ret = 0
    mult = floor(log10(n_abs))
    while n_abs > 0:
        ret += (n_abs % 10) * (10 ** mult)
        mult -= 1
        n_abs //= 10
    return ret * (-1 if n < 0 else 1)