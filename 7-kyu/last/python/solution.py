def last(*args):
    if len(args) == 1:
        try:
            return args[-1][-1]
        except:
            return args[0]
    return args[-1]