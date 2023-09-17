def is_nice(arr):
    if not arr:
        return False
    return all((n + 1 in arr) or (n - 1 in arr) for n in arr)