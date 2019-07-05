def pattern(n):
    ret = []
    for i in range(1, n + 1):
        to_append = ''
        to_append += ''.join(str(j) for j in range(i, n + 1))
        to_append += ''.join(str(j) for j in range(1, i))
        ret.append(to_append)
    return '\n'.join(ret)