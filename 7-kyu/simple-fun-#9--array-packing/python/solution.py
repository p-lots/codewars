def array_packing(arr):
    while len(arr) < 4:
        arr.append(0)
    arr = arr[::-1]
    ret = 0
    ret = ret | (arr[0] << 24)
    ret = ret | (arr[1] << 16)
    ret = ret | (arr[2] << 8)
    ret = ret | arr[3]
    return ret