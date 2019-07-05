def pythagorean_triple(integers):
    integers = sorted(integers)
    a = integers[0]
    b = integers[1]
    c = integers[2]
    return a ** 2 + b ** 2 == c ** 2