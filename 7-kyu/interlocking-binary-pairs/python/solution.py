def interlockable(a, b):
    
    if a == 0 or b == 0:
        return True
    elif a == b:
        return False
    ptr = 1
    greater = max(a, b)
    while ptr < greater:
        if a & ptr == b & ptr and (a & ptr) != 0 and (b & ptr) != 0:
            return False
        ptr <<= 1
    return True
