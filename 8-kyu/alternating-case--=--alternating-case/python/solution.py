def to_alternating_case(strng):
    return ''.join(ch.lower() if ch.isupper() else ch.upper() for ch in strng)