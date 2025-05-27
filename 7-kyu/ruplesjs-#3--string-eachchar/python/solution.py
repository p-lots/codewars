def each_char(strng, arg):
    if isinstance(arg, str):
        return ''.join(ch + arg for ch in strng)
    return ''.join(map(arg, strng))