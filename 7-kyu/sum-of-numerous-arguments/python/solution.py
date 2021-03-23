def find_sum(*args):
    if not args:
        return 0
    elif any(n < 0 for n in args):
        return -1
    return sum(args)