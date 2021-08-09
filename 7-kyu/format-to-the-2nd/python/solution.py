def print_nums(*args):
    if not args:
        return ''
    longest_n = max(map(lambda elem: len(str(elem)), args))
    return '\n'.join(str(n).zfill(longest_n) for n in args)
