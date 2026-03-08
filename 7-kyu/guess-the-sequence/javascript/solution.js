def sequence(x):
    seq = [str(n) for n in range(1, x + 1)]
    return [int(n) for n in sorted(seq)]
