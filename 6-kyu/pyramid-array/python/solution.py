def pyramid(n):
    return [[1] * i for i in range(1, n + 1)] if n > 0 else []
