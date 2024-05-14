from math import gcd

def reduce_fraction(fraction):
    numer, denom = fraction
    hcf = gcd(numer, denom)
    return (numer / hcf, denom / hcf)
