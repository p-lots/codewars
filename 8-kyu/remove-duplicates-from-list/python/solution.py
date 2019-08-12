def distinct(seq):
    ret = []
    for item in seq:
        if ret.count(item) == 0:
            ret.append(item)
    return ret