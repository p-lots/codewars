import string

def switcher(arr):
    ret = ''
    for n in arr:
        n = int(n)
        if n < 27 and n > 0:
            ret += chr((26 - n) + ord('a'))
        elif n == 27:
            ret += '!'
        elif n == 28:
            ret += '?'
        elif n == 29:
            ret += ' '
    return ret