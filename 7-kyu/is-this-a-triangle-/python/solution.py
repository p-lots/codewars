def is_triangle(a, b, c):
    smallest, middle, largest = sorted([a, b, c])
    return smallest + middle > largest