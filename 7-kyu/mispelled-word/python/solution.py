def hamming_distance(word1, word2):
    return sum(1 for ch1, ch2 in zip(word1, word2) if ch1 != ch2)

def mispelled(word1, word2):
    if len(word1) == 0 and len(word2) == 0:
        return True
    if len(word1) == 0 or len(word2) == 0:
        return False
    if abs(len(word1) - len(word2)) > 1:
        return False
    elif abs(len(word1) - len(word2)) == 1:
        longer = max(word1, word2, key=len)
        shorter = min(word2, word2, key=len)
        return hamming_distance(longer[1:], shorter) <= 1 or hamming_distance(longer[:-1], shorter) <= 1
    return hamming_distance(word1, word2) <= 1
        