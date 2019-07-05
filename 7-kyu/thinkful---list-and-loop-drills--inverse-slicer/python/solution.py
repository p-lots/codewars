def inverse_slice(items, a, b):
    ret = []
    for i, x in enumerate(items):
        if i >= a and i < b:
            continue
        ret.append(x)
    return ret