def equable_triangle(a, b, c):
    perimeter = a + b + c
    half = perimeter / 2
    area = (half * (half - a) * (half - b) * (half - c)) ** 0.5
    return perimeter == area