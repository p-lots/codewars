def div_con(x):
    strs = [int(n) for n in x if isinstance(n, str)]
    ints = [n for n in x if isinstance(n, int)]
    return sum(ints) - sum(strs)