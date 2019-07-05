def is_opposite(s1,s2):
    if not s1 or not s2:
        return False
    return s1 == ''.join(ch.lower() if ch.isupper() else ch.upper() for ch in s2)