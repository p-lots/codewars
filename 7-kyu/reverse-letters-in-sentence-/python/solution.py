def reverser(sentence):
    ret = ''
    word = ''
    for ch in sentence:
        if ch.isspace():
            ret += word[::-1]
            ret += ch
            word = ''
        elif ch.isalpha():
            word += ch
    ret += word[::-1]
    return ret
