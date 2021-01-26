def filter_homogenous(arrays):
    return [arr for arr in arrays if arr and (all(type(elem) == str for elem in arr) or all(type(elem) == int for elem in arr))]
