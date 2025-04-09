from collections import Counter

def unscramble(scramble):
    global word_list # available in preloaded
    return [word for word in word_list if Counter(word) == Counter(scramble)]
