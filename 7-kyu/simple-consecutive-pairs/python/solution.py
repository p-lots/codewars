def pairs(ar):
    if len(ar) % 2 == 1:
        ar = ar[:-1]
    return sum(1 if abs(ar[i] - ar[i + 1]) == 1 else 0 for i in range(0, len(ar), 2))
