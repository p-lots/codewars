def sum_from_string(strng):
    ret = 0
    curr_n = ''
    for ch in strng:
        if ch.isdigit():
            curr_n += ch
        else:
            if curr_n:
                ret += int(curr_n)
                curr_n = ''
    if curr_n:
        ret += int(curr_n)
    return ret
