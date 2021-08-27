def vowel_count(word):
    return len([ch for ch in word if ch.lower() in 'aeiou'])

def cons_count(word):
    return len([ch for ch in word if ch.lower() not in 'aeiou'])

def i(word):
    return f'i{word}' if word and (word[0].lower() != 'i' and vowel_count(word) < cons_count(word) and word[0].isupper()) else 'Invalid word'
