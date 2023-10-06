from itertools import groupby

def set_reducer(inp):
    if len(inp) == 1:
        return inp[0]
    groups = [list(g) for k, g in groupby(inp)]
    next_inp = [len(group) if len(group) > 1 else 1 for group in groups]
    return set_reducer(next_inp)
