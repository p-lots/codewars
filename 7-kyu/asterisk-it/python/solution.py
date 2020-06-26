def asterisc_it(n): 
    if type(n) == int:
        n = str(n)
    elif type(n) == list:
        n = ''.join(str(item) for item in n)
    ret = n[0]
    for x, y in zip(n, n[1:]):
        if int(x) % 2 == 0 and int(y) % 2 == 0:
            ret += f'*{y}'
        else:
            ret += y
    return ret