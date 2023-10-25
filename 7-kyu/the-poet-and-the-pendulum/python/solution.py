def pendulum(values):
    ret = []
    values = sorted(values)
    nxt = values.pop(0)
    i = 0
    while values:
        if i % 2 == 0:
            ret.insert(0, nxt)
        else:
            ret.append(nxt)
        nxt = values.pop(0)
        i += 1
    if i % 2 == 0:
        ret.insert(0, nxt)
    else:
        ret.append(nxt)
    return ret
