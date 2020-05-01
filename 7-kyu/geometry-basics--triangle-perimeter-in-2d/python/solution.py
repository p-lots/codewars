from math import sqrt

def dist(a, b):
    return sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)

def triangle_perimeter(triangle):
    ret = dist(triangle.a, triangle.b) + dist(triangle.b, triangle.c) + dist(triangle.a, triangle.c)
    return round(ret, 6)