def first_non_consecutive(arr):
    n = arr[0]
    for number in arr:
        if n != number:
            return number
        n += 1
    return None