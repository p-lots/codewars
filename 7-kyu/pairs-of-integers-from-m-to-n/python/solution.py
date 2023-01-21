def generate_pairs(m, n):
    ret = []
    for i in range(m, n + 1):
        for j in range(i, n + 1):
            ret.append((i, j))
    return ret