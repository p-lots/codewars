def meeting(s):
    names = [tuple(name.split(':')[::-1]) for name in s.upper().split(';')]
    names_sorted = sorted(names, key=lambda elem: (elem[0], elem[1]))
    return ''.join(f'({name[0]}, {name[1]})' for name in names_sorted)