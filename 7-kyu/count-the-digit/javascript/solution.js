def nb_dig(n, d):
    arr = list(filter(lambda num: str(d) in num, [str(i * i) for i in range(n + 1)]))
    ret = 0
    for num in arr:
        for ch in num:
            if ch == str(d):
                ret += 1
    return ret