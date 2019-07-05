def reverse(a):
    a_rev = ''.join(list(reversed(''.join(a))))
    ret = []
    start = 0
    for word in a:
        ret.append(a_rev[start:(start+len(word))])
        start += len(word)
    return ret