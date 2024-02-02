def add(*args):
    return round(sum(num / idx for idx, num in enumerate(args, 1)))
