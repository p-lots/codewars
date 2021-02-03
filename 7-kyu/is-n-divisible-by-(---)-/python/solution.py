def is_divisible(*args):
    return all(args[0] % n == 0 for n in args)
