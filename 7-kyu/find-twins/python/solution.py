def elimination(arr):
    for n in arr:
        if arr.count(n) == 2:
            return n