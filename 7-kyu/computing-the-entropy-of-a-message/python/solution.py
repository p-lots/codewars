import math

def entropy(message: str) -> float:
    no_spaces = [ch for ch in message if not ch.isspace()]
    total_symbols = len(no_spaces)
    if not message or not total_symbols:
        return 0.0
    total = 0.0
    for ch in set(no_spaces):
        total += (no_spaces.count(ch) / total_symbols) * math.log2(no_spaces.count(ch) / total_symbols)
    return -total
