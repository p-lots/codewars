from math import gcd

def binary_gcd(x, y):
    return f'{gcd(x, y):b}'.count('1')