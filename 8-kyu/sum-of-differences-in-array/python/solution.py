def sum_of_differences(arr):
    if len(arr) < 2:
        return 0
    arr = sorted(arr, reverse=True)
    return sum(first - second for first, second in zip(arr, arr[1:]))
