def remove(s, n):
    ret = ''
    for ch in s:
        if ch == '!' and n > 0:
            n -= 1
            continue
        ret += ch
    return ret