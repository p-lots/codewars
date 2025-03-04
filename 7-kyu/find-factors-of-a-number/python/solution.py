def factors(x):
    if not isinstance(x, int) or x < 1:
        return -1
    return [n for n in range(1, x + 1) if x % n == 0][::-1]
