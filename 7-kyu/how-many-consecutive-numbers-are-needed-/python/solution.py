def consecutive(arr):
    if not arr:
        return 0
    start = min(arr)
    end = max(arr)
    return abs(len(arr) - len(range(start, end + 1)))