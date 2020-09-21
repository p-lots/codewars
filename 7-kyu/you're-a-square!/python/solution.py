from math import sqrt

def is_square(n):    
    if n < 0:
        return False
    root = int(sqrt(n))
    return root ** 2 == n
