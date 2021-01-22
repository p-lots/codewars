def geometric_sequence_elements(a, r, n):
    ret = [a]
    for _ in range(n - 1):
        ret.append(ret[-1] * r)
    return ', '.join(str(n) for n in ret)
