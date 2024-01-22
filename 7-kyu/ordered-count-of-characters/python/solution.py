from collections import Counter

def ordered_count(inp):
    char_counts = Counter(inp)
    return sorted([(k, v) for k, v in char_counts.items()], key=lambda c: inp.index(c[0]))