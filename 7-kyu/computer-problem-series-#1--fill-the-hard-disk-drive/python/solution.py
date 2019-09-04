def save(sizes, hd):
    if not sizes:
        return 0
    if sizes[0] > hd:
        return 0
    ret = []
    while sizes and sum(ret) < hd:
        ret.append(sizes.pop(0))
        if sizes and sizes[0] + sum(ret) > hd:
            break
    return len(ret)