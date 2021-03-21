def sum_nested(lst):
    ret = 0
    for elem in lst:
        if not elem:
            continue
        if type(elem) == list:
            ret += sum_nested(elem)
        elif type(elem) == int:
            ret += elem
    return ret
