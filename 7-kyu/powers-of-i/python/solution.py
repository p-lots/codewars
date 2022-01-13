def pofi(n):
    n %= 4
    if n == 0:
        return '1'
    elif n == 1:
        return 'i'
    elif n == 2:
        return '-1'
    elif n == 3:
        return '-i'
