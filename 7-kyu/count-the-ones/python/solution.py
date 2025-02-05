def hamming_weight(x):
    ones_count = 0
    while x:
        if x & 1:
            ones_count += 1
        x >>= 1
    return ones_count
