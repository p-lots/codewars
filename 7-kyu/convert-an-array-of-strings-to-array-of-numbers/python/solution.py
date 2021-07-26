def to_float_array(arr):
    return [float(elem) if type(elem) == str else elem for elem in arr]
