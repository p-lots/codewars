def sum_array(arr):
    if not arr:
        return 0
    arr = sorted(arr)
    return sum(arr[1:-1])