def move_ten(st):
    ret = ''
    for ch in st:
        new_ch = ord(ch) + 10
        if new_ch > ord('z'):
            new_ch -= 26
        ret += chr(new_ch)
    return ret