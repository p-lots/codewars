def print_array(arr):
    return ','.join(str(elem) if not isinstance(elem, str) else elem for elem in arr)