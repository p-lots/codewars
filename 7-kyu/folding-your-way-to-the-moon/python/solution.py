from math import log2, ceil

def fold_to(distance):
    if distance < 0:
        return None
    elif distance < 0.0001:
        return 0
    return ceil(log2(distance / 0.0001))