def tetration(x, y):
    if y == 0:
        return 1
    ret = x
    for _ in range(y - 1):
        ret = x ** ret
    return ret
