def next_letter(s):
    ret = ''
    for l in s:
        if l.isalpha():
            l_ord = ord(l) + 1
            if l_ord == 91 or l_ord == 123:
                l_ord -= 26
            ret += chr(l_ord)
        else:
            ret += l
    return ret