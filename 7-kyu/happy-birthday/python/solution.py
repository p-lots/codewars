def wrap(*args):
    short, mid, long = sorted(args)
    return 20 + (mid * 2 + short * 2) + (long * 2 + short * 2)