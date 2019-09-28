def negation_value(s, val):
    if not s:
        return bool(val)
    while s:
        val = not val
        s = s[1:]
    return val