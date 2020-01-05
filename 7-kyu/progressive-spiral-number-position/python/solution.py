def layers(n):
    if n == 1:
        return 1
    p = 1
    pow_res = 1
    ret = 0
    while pow_res < n:
        pow_res = p * p
        ret += 1
        p += 2
    return ret