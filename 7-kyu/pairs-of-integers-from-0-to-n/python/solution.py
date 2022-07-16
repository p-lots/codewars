def generate_pairs(n):
    ret = []
    for i in range(n + 1):
        for j in range(n + 1):
            next_pair = sorted([i, j])
            if next_pair not in ret:
                ret.append(next_pair)
    return ret