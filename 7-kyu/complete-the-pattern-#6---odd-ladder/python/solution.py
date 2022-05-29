def pattern(n):
    if n > 0 and n % 2 == 0:
        n -= 1
    return '\n'.join(str(i) * i for i in range(1, n + 1, 2))
