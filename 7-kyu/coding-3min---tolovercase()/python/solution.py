import string

LOVE = 'LOVE'

def to_lover_case(strng):
    ret = ''
    for ch in strng:
        if str.isalpha(ch):
            love_pos = string.ascii_lowercase.index(ch.lower()) % 4
            ret += LOVE[love_pos]
        else:
            ret += ch
    return ret