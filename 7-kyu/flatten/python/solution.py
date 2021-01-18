def flatten(lst):
    ret = []
    for elem in lst:
        if type(elem) == list:
            for subelem in elem:
                ret.append(subelem)
        else:
            ret.append(elem)
    return ret
