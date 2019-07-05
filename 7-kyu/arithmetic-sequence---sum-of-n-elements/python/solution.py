def arithmetic_sequence_sum(a, r, n):
    ret = 0
    for x in range(n):
        ret += a
        for _ in range(x):
            ret += r
    return ret