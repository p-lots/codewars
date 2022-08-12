from collections import defaultdict

def switch_dict(d):
    ret = defaultdict(list)
    for k, v in d.items():
        ret[v].append(k)
    return ret
