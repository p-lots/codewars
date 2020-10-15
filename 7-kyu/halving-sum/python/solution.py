def halving_sum(n):
    ret = n
    next = n // 2
    while next > 0:
        ret += next
        next //= 2
    return ret