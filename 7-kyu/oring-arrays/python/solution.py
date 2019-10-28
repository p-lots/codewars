def or_arrays(arr1, arr2, default=0):
    while len(arr1) != len(arr2):
        if len(arr1) < len(arr2):
            arr1.append(default)
        elif len(arr2) < len(arr1):
            arr2.append(default)
    return list(map(lambda pair: pair[0] | pair[1], zip(arr1, arr2)))