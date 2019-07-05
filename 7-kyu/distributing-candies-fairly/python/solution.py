def distribute(m, n):
    if n <= 0:
        return []
    m = max(m, 0)
    ret = [0 for x in range(n)]
    i = 0
    while m > 0:
        ret[i % n] += 1
        m -= 1
        i += 1
    return ret