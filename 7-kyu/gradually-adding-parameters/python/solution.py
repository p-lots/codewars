def add(*args):
    return sum(i * n for i, n in enumerate(args, 1))
