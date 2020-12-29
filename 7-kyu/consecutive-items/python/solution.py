def consecutive(arr, a, b):
    for x, y in zip(arr, arr[1:]):
        if (x == a or x == b) and (y == a or y == b):
            return True
    return False
