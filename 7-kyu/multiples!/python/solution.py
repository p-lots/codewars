def multiple(x):
    ret = ''
    if x % 3 == 0:
        ret += 'Bang'
    if x % 5 == 0:
        ret += 'Boom'
    return ret if ret else 'Miss'
