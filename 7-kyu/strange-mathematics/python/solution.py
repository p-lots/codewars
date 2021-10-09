def strange_math(n, k):
    ret = sorted(str(num) for num in range(0, n + 1))
    return ret.index(str(k))
