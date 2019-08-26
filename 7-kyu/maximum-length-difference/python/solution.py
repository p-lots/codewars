def mxdiflg(a1, a2):
    if not a1 or not a2:
        return -1
    a1_sorted = sorted(a1, key=len)
    a2_sorted = sorted(a2, key=len)
    return max(abs(len(a1_sorted[-1]) - len(a2_sorted[0])), abs(len(a2_sorted[-1]) - len(a1_sorted[0])))