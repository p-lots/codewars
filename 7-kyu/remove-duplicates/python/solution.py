def unique(integers):
    ret = []
    for n in integers:
        if n not in ret:
            ret.append(n)
    return ret
