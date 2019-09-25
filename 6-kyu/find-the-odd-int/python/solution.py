def find_it(seq):
    for item in seq:
        if seq.count(item) % 2 == 1:
            return item
    return None
