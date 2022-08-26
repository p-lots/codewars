def find_e(s):
    if not s:
        return s
    ret = sum(ch.lower() == 'e' for ch in s)
    return str(ret) if ret else 'There is no "e".'
