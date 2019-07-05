def remove(s, n):
    ret = ''
    for ch in s:
        if ch != '!':
            ret += ch
        else:
            if n > 0:
                n -= 1
            else:
                ret += ch
    return ret