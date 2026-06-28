def array_center(arr):
    smallest = min(arr)
    avg = sum(arr) / len(arr)
    return [n for n in arr if abs(n - avg) < smallest]