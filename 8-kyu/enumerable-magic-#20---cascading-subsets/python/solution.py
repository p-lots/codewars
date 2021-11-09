def each_cons(lst, n):
    ret = []
    i = 0
    while i + n <= len(lst):
        ret.append(lst[i:i + n])
        i += 1
    return ret
