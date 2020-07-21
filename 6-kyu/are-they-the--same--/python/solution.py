def comp(array1, array2):
    return sorted([n * n for n in array1]) == sorted(array2) if array1 != None and array2 != None else False