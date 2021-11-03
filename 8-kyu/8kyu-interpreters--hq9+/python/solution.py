def _H():
    return 'Hello World!'

def _Q(arg):
    return arg

def _9():
    ret = []
    next_str = ''
    for n in range(99, -1, -1):
        if n != 0:
            bottle_s = f'bottle{"s" if n > 1 else ""}'
            next_str = f'{n} {bottle_s} of beer on the wall, {n} {bottle_s} of beer.\nTake one down and pass it around, {n - 1 if n > 1 else "no more"} bottle{"s" if n - 1 != 1 else ""} of beer on the wall.'
        else:
            next_str = 'No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.'
        ret.append(next_str)
    return '\n'.join(ret)

def HQ9(code):
    if code == 'H':
        return _H()
    elif code == 'Q':
        return _Q(code)
    elif code == '9':
        return _9()
    return None
