from collections import Counter

def grabscrab(word, possible_words):
    word_counter = Counter(word)
    possible_words_counter = [(Counter(item), item) for item in possible_words]
    return [item[1] for item in possible_words_counter if item[0] == word_counter]