import re

def pluralize(word):
    es_endings = ['s', 'x', 'z', 'ch', 'sh']
    for ending in es_endings:
        if word.endswith(ending):
            return f'{word}es'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    for cons in consonants:
        if word.endswith(f'{cons}y'):
            return re.sub(r'(.*)y', r'\1ies', word)
    return f'{word}s'
