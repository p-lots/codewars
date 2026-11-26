import math

def moser():
    n = 0
    while True:
        n += 1
        yield math.comb(n, 4) + math.comb(n, 2) + 1