def kebabize(strng):
    ret = ''
    strng = ''.join(ch for ch in strng if ch.isalpha())
    for i, ch in enumerate(strng):
        if ch.islower():
            ret += ch
        elif ch.isupper():
            if i > 0:
                ret += '-'
            ret += ch.lower()
    return ret