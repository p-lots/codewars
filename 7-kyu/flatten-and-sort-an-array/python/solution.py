def flatten_and_sort(array):
    ret = []
    for arr in array:
        for n in arr:
            ret.append(n)
    return sorted(ret)