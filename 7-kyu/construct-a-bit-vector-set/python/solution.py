def sort_by_bit(seq):
    ret = [0] * 32
    for n in seq:
        ret[31 - n] = 1
    return int(''.join(str(n) for n in ret), 2)
