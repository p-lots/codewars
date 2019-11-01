def squares(x, n):
    if n < 1:
        return []
    ret = [x]
    for _ in range(1, n):
        ret.append(ret[-1] * ret[-1])
    return ret