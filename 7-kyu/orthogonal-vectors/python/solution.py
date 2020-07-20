from functools import reduce

def is_orthogonal(u, v): 
    return reduce(lambda accum, nxt: accum + nxt[0] * nxt[1], zip(u, v), 0) == 0