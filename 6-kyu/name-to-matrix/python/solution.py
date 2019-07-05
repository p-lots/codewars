from math import ceil, sqrt

def matrixfy(st):
    if len(st) == 0:
        return "name must be at least one letter"
    idx = 0
    length = ceil(sqrt(len(st)))
    ret = []
    for x in range(length):
        row = []
        for y in range(length):
            row.append(st[idx] if idx < len(st) else '.')
            idx += 1
        ret.append(row)
    return ret