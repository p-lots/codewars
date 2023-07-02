def deep_count(a):
    ret = len(a)
    for elem in a:
        if isinstance(elem, list):
            ret += deep_count(elem)
    return ret
