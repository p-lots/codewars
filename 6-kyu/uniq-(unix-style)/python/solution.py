def uniq(seq):
    if not seq:
        return seq
    ret = [seq[0]]
    for elem in seq[1:]:
        if elem != ret[-1]:
            ret.append(elem)
    return ret