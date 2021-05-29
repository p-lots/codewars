def hotpo(n):
    ret = 0
    while n > 1:
        n = (n // 2 if n % 2 == 0 else n * 3 + 1)
        ret += 1
    return ret
