def swap(strng):
    return ''.join(ch.upper() if ch.islower() else ch.lower() for ch in strng)