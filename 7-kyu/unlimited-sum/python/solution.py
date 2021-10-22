def sum(*args):
    ret = 0
    for n in args:
        if isinstance(n, int):
            ret += n
    return ret