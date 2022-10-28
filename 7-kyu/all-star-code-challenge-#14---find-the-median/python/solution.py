def median(array):
    array = sorted(array)
    mid = len(array) // 2
    return array[mid] if len(array) % 2 == 1 else (array[mid - 1] + array[mid]) / 2
