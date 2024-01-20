def distinct(seq):
    return sorted(set(seq), key=lambda elem: seq.index(elem))