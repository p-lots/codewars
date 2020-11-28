def compose(s1, s2):
    s1 = s1.split()
    s2 = s2.split()
    ret = []
    for n in range(len(s1)):
        p1 = s1[n][:n + 1]
        p2 = s2[-(n + 1)][:-n] if n > 0 else s2[-(n + 1)][:]
        to_append = p1 + p2
        ret.append(to_append)
    return '\n'.join(ret)