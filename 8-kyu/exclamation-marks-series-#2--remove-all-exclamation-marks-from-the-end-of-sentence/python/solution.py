def remove(s):
    if s:
        while s[-1] == '!':
            s = s[:-1]
    return s