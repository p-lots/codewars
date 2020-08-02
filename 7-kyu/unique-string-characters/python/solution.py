def solve(a, b):
    ret = ''
    for ch in a:
        if ch not in b:
            ret += ch
    for ch in b:
        if ch not in a:
            ret += ch
    return ret