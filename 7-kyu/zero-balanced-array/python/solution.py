def is_zero_balanced(arr):
    if not arr:
        return False
    for n in arr:
        if arr.count(-n) != arr.count(n):
            return False
    return True
