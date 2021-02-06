def triple_x(s):
    try:
        first_x = s.index('x')
    except:
        return False
    return s[first_x:first_x + 3] == 'xxx'