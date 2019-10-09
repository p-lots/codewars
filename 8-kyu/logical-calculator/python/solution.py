from functools import reduce

def logical_calc(array, op):
    if op == "AND":
        return reduce(lambda acc, item: acc and item, array)
    if op == "OR":
        return reduce(lambda acc, item: acc or item, array)
    if op == "XOR":
        return reduce(lambda acc, item: acc ^ item, array)