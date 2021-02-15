def solve(arr):
    arr_cpy = arr[:]
    ret = []
    while arr_cpy:
        ret.append(max(arr_cpy))
        del arr_cpy[arr_cpy.index(max(arr_cpy))]
        if arr_cpy:
            ret.append(min(arr_cpy))
            del arr_cpy[arr_cpy.index(min(arr_cpy))]
    return ret
