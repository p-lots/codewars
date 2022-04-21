def typist(s):
    ret = len(s)
    if s and s[0].isupper():
        ret += 1
    for first, second in zip(s, s[1:]):
        if not (first.isupper() == second.isupper()):
            ret += 1
    return ret
