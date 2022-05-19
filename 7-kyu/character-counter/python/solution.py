from collections import Counter

def validate_word(word):
    counts = Counter(word.lower())
    counts_val = list(counts.values())
    return all(first == second for first, second in zip(counts_val, counts_val[1:]))
