import math

def get_area(shape):
    return shape[0] * shape[1] if isinstance(shape, tuple) else math.pi * shape * shape

def sort_by_area(seq):
    return sorted(seq, key=get_area)
