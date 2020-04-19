def pattern(n):
    return '\n'.join(''.join(str(y) for y in range(x, n + 1)) for x in range(1, n + 1)) if n >= 1 else ''