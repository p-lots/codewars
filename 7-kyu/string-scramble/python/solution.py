def scramble(strng, array):
    ret = ['*'] * len(strng)
    for idx, ch in enumerate(strng):
        ret[array[idx]] = ch
    return ''.join(ret)
