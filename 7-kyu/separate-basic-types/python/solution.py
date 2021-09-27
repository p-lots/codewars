from collections import defaultdict

def separate_types(seq): 
    ret = defaultdict(list)
    for elem in seq:
        ret[type(elem)].append(elem)
    return ret