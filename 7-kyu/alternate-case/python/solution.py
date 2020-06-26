def alternateCase(s):
    return ''.join([ch.lower() if ch.isupper() else ch.upper() for ch in s])