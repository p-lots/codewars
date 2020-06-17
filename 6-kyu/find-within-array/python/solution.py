def find_in_array(seq, predicate): 
    for idx, val in enumerate(seq):
        if predicate(val, idx):
            return idx
    return -1