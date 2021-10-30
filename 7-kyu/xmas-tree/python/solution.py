def xmastree(n):
    ret = [('_' * (n - i)) + ('#' * (i * 2 - 1)) + ('_' * (n - i)) for i in range(1, n + 1)]
    ret.append(('_' * (n - 1)) + '#' + ('_' * (n - 1)))
    ret.append(('_' * (n - 1)) + '#' + ('_' * (n - 1)))
    return ret
