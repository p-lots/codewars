def least_larger(a, i):
    differences = {idx: n - a[i] for idx, n in enumerate(a)}
    ret = (-1, float('inf'))
    for k, v in differences.items():
        if 0 < v < ret[1]:
            ret = (k, v)
    return ret[0]