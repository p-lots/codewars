def freq_seq(s, sep):
    ret = []
    for ch in s:
        ret.append(str(s.count(ch)))
    return sep.join(ret)