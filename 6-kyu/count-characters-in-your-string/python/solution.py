def count(string):
    ret = {}
    for ch in string:
        if ch not in ret:
            ret[ch] = 1
        else:
            ret[ch] += 1
    return ret