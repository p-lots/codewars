def box(n):
    top = '-' * n
    mid = f'-{" " * (n - 2)}-'
    return [top] + [mid] * (n - 2) + [top]
