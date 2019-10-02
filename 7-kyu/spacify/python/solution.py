def spacify(strng):
    if len(strng) <= 1:
        return strng
    return ' '.join(ch for ch in strng)