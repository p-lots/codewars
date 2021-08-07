def unused_digits(*args):
    used = set(''.join(str(n) for n in args))
    return ''.join(filter(lambda elem: elem not in used, '0123456789'))
