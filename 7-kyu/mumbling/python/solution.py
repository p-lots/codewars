def accum(s):
    return '-'.join((letter*(i + 1)).title() for i, letter in enumerate(s.lower()))