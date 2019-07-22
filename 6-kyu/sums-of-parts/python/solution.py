def parts_sums(ls):
    if not ls:
        return [0]
    ret = []
    ls_sum = sum(ls)
    ret.append(ls_sum)
    for n in ls:
        ret.append(ls_sum - n)
        ls_sum -= n
    return ret