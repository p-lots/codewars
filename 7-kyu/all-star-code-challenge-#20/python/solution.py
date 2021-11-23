def add_arrays(array1, array2): 
    if len(array1) != len(array2):
        raise Exception
    return [x + y for x, y in zip(array1, array2)]
