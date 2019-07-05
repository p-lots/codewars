def paul(x):
    lookup_table = { 'kata': 5, 'Petes kata': 10, 'life': 0, 'eating': 1 }
    ret = sum(map(lambda a: lookup_table[a], x))
    if ret >= 100:
        return 'Miserable!'
    elif ret >= 70:
        return 'Sad!'
    elif ret >= 40:
        return 'Happy!'
    else:
        return 'Super happy!'
    