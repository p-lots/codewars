def procedure(i):
    ret = [i * j for j in range(1, 11) if i * j <= 100]
    return sum(sum(map(int, str(n))) for n in ret)
