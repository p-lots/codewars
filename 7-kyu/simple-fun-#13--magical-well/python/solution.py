def magical_well(a, b, n):
    ret = 0
    while n > 0:
        ret += a * b
        a += 1
        b += 1
        n -= 1
    return ret
