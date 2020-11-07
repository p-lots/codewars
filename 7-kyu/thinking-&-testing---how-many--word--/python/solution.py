def testit(s):
    ret = 0
    w_idx, o_idx, r_idx = None, None, None
    for i, ch in enumerate(s.lower()):
        if ch == 'w':
            w_idx = i
        elif ch == 'o' and w_idx != None:
            o_idx = i
        elif ch == 'r' and w_idx != None and o_idx != None:
            r_idx = i
        elif ch == 'd' and w_idx != None and o_idx != None and r_idx != None:
            ret += 1
            w_idx = o_idx = r_idx = None
    return ret