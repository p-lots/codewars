def find_2nd_largest(arr):
    if not arr:
        return None
    arr = [item for item in arr if type(item) == int]
    if not arr:
        return None
    arr = sorted(arr, reverse=True)
    if arr[0] == arr[1]:
        return None
    return arr[1]