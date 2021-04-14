def toCsvText(array):
    return '\n'.join(','.join(str(elem) for elem in arr) for arr in array)