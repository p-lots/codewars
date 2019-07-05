def scale(strng, k, n):
    if not strng:
        return ''
    ret = []
    for line in strng.split('\n'):
        temp = ''
        for ch in line:
            temp += ''.join(ch for _ in range(k))
        for _ in range(n):
            ret.append(temp)
    return '\n'.join(ret)