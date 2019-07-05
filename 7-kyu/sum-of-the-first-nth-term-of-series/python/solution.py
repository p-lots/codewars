def series_sum(n):
    ret = 0
    for i in range(n):
        ret += 1 / (i * 3 + 1)
    return "{:.2f}".format(ret)