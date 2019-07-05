def first_reverse_try(arr):
    if not arr:
        return arr
    arr[0], arr[len(arr) - 1] = arr[len(arr) - 1], arr[0]
    return arr