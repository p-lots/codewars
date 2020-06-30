def complete_series(seq): 
    if len(set(seq)) != len(seq):
        return [0]
    seq = sorted(seq)
    if len(range(seq[-1] + 1)) == len(seq):
        return seq
    return list(range(seq[-1] + 1))