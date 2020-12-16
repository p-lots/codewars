def arr2bin(arr):
    return bin(sum(arr))[2:] if all(type(elem) == int for elem in arr) else False
