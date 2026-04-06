def remove_vowels(word):
    return ''.join(ch if ch.lower() not in 'aeiou' else '' for ch in word)

def small_word_helper(sentence):
    return ' '.join(word.upper() if len(word) < 4 else remove_vowels(word) for word in sentence.split(' '))