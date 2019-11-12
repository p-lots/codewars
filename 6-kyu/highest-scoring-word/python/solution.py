def get_word_score(word):
    return sum(ord(ch) - ord('a') + 1 for ch in word)

def high(x):
    return max(x.split(), key=get_word_score)