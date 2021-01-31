def longest_word(string_of_words):
    return max(string_of_words.split()[::-1], key=len)
