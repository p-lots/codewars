def neutralise(s1, s2):
    s1_split = [ord(ch) - 44 for ch in s1]
    s2_split = [ord(ch) - 44 for ch in s2]
    ret = []
    for lhs, rhs in zip(s1_split, s2_split):
        # ord('+') == 43
        # ord('-') == 45
        match lhs + rhs:
            case 2:
                ret.append('-')
            case 0:
                ret.append('0')
            case -2:
                ret.append('+')
    return ''.join(ret)
