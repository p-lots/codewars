def remainder(a, b):
    small, large = min(a, b), max(a, b)
    return large % small if small != 0 else None
