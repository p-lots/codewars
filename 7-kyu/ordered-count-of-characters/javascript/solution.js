def ordered_count(input):
    char_counts = {}
    for ch in input:
        if ch not in char_counts:
            char_counts[ch] = 1
        else:
            char_counts[ch] += 1
    ret = []
    for k, v in char_counts.items():
        ret.append((k, v))
    ret = sorted(ret, key=lambda c: input.index(c[0]))
    return ret