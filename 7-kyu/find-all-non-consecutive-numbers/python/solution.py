def all_non_consecutive(arr):
    ret = []
    if len(arr) <= 1:
        return ret
    expected = arr[0]
    for i, actual in enumerate(arr):
        if expected != actual:
            ret.append({'i': i, 'n': actual})
            expected = actual
        expected += 1
    return ret