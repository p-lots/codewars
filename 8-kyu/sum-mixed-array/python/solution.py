def sum_mix(arr):
    arr_int = [int(item) if type(item) == str else item for item in arr]
    return sum(arr_int)