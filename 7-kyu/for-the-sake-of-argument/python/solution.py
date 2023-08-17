def numbers(*args):
    return all(type(num) == float or type(num) == int for num in args)
