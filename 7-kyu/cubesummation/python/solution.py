def cube_sum(n, m):
    start, end = min(n, m), max(n, m)
    return sum(num ** 3 for num in range(start + 1, end + 1))
