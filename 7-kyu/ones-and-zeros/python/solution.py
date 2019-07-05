def binary_array_to_number(arr):
    ret = 0
    for n in arr:
        ret = ret << 1
        if n == 1:
            ret = ret | 1
    return ret