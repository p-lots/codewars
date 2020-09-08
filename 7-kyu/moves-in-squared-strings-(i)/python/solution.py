def vert_mirror(strng):
    return '\n'.join(line[::-1] for line in strng.split())
def hor_mirror(strng):
    return '\n'.join(line for line in reversed(strng.split()))
def oper(fct, s):
    return fct(s)
