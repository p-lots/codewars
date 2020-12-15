import math

def circleArea(r):
    if type(r) != float and type(r) != int:
        return False
    if r <= 0:
        return False
    return round(r ** 2 * math.pi, 2)
