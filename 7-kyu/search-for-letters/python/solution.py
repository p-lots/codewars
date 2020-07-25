from string import ascii_lowercase

def change(st):
    ret = [0] * 26
    for ch in st:
        if ch.isalpha():
            idx = ascii_lowercase.index(ch.lower())
            ret[idx] = 1
    return ''.join(str(n) for n in ret)