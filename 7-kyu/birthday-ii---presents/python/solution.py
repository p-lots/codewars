def present(x,y):
    if x == 'goodpresent':
        return ''.join(chr(ord(ch) + y) for ch in x)
    elif x == 'crap' or x == 'empty':
        return ''.join(sorted(x))
    elif x == 'bang':
        return str(sum(ord(ch) - y for ch in x))
    elif x == 'badpresent':
        return 'Take this back!'
    elif x == 'dog':
        return 'pass out from excitement {} times'.format(y)