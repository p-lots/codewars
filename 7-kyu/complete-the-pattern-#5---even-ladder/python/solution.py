def pattern(n):
    return '\n'.join(str(step) * step for step in range(2, n + 1, 2))
