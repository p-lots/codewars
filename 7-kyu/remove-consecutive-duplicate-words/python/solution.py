def remove_consecutive_duplicates(s):
    if not s:
        return ''
    s = s.split()
    ret = [s[0]]
    while s:
        if s[0] != ret[-1]:
            ret.append(s[0])
        s.pop(0)
    return ' '.join(ret)
        