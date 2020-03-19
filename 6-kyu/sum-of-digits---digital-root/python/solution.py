def digital_root(n):
    n = sum(map(int, str(n)))
    return digital_root(n) if n > 10 else n