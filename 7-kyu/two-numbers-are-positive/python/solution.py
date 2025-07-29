def two_are_positive(*args):
    positives = [n for n in args if n > 0]
    return len(positives) == 2
