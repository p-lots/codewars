def hamming_distance(a, b):
    ret = 0
    a_str = f'{a:b}'
    b_str = f'{b:b}'
    if len(a_str) < len(b_str):
        a_str = a_str.zfill(len(b_str))
    if len(b_str) < len(a_str):
        b_str = b_str.zfill(len(a_str))
    return sum(lhs != rhs for lhs, rhs in zip(a_str, b_str))
