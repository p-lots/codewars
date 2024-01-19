from collections import defaultdict

def merge(*dicts):
    ret = defaultdict(list)
    for dct in dicts:
        for key, val in dct.items():
            ret[key].append(val)
    return ret