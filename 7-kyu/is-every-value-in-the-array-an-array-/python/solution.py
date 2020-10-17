def arr_check(arr):
    return all(isinstance(elem, list) for elem in arr)