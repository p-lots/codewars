def unique_in_order(iterable):
    ret = []
    if not iterable:
        return ret
    prev = iterable[0]
    ret.append(prev)
    for i in range(1, len(iterable)):
        if iterable[i] != prev:
            ret.append(iterable[i])
        prev = iterable[i]
    return ret