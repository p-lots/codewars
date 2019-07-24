def avg_array(arrs):
    ret = []
    if not arrs:
        return ret
    for j in range(len(arrs[0])):
        total = 0
        for i in range(len(arrs)):
            total += arrs[i][j]
        total /= len(arrs)
        ret.append(total)
    return ret