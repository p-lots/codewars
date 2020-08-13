def next_id(arr):
    if not arr:
        return 0
    for id in range(max(arr) + 2):
        if id not in arr:
            return id