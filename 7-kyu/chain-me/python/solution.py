from functools import reduce

def chain(init_val, functions):
    return reduce(lambda accum, nxtfunc: nxtfunc(accum), functions, init_val)
