def remove(s):
    ret = ''
    found_start = False
    for ch in s[::-1]:
        if ch == '!':
            if not found_start:
                ret += ch
        else:
            if not found_start and ch.isalpha():
                found_start = True
            ret += ch
    return ret[::-1]
