def diff(a, b):
    a_set = set(a)
    b_set = set(b)
    return sorted(list(a_set.symmetric_difference(b_set)))