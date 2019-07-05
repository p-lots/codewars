def mirror(code, flip='abcdefghijklmnopqrstuvwxyz'):
    lookup_table = {}
    for i in range(len(flip)):
        lookup_table[flip[i]] = flip[len(flip) - i - 1]
    ret = ''
    for ch in code.lower():
        if ch in lookup_table:
            ret += lookup_table[ch]
        else:
            ret += ch
    return ret