def highest_value(a, b):
    return a if sum(ord(ch) for ch in a) >= sum(ord(ch) for ch in b) else b
