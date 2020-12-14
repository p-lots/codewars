def alphabetic(s):
    s = s.lower()
    return all(ord(x) <= ord(y) for x, y in zip(s, s[1:]))
