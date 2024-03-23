def count_consonants(text):
    consonants = [ch for ch in text.lower() if ch.isalpha() and ch not in 'aeiou']
    return len(set(consonants))