from collections import defaultdict

def stem_and_leaf(data):
    ret = defaultdict(list)
    for elem in sorted(data):
        stem = elem // 10
        leaf = elem % 10
        ret[stem].append(leaf)
    return ret