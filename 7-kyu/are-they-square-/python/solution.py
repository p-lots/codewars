def is_square(arr):
    return all(int(n ** 0.5) ** 2 == n for n in arr) if arr else None
