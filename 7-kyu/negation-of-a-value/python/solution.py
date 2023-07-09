def negation_value(s, val):
    val = bool(val)
    if not s:
        return val
    return not val if len(s) % 2 == 1 else val