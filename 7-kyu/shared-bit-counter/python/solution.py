def shared_bits(a, b):
    ret = 0
    a, b = f'{a:b}', f'{b:b}'
    a = a.zfill(len(b))
    b = b.zfill(len(a))
    for na, nb in zip(a, b):
        if na == '1' and nb == '1':
            ret += 1
    return ret > 1
