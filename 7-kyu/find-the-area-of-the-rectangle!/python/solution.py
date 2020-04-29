from math import sqrt

def area(d, l):
    if d <= l:
        return 'Not a rectangle'
    w = sqrt(d ** 2 - l ** 2)
    return round(w * l, 2)