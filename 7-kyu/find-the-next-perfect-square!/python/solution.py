from math import sqrt

def find_next_square(sq):
    root = sqrt(sq)
    if int(root) * int(root) != sq:
        return -1
    return (root + 1) ** 2
