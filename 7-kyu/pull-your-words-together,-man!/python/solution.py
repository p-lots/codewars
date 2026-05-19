def sentencify(words):
    sentence = ' '.join(words)
    return f'{sentence[0].upper()}{sentence[1:]}.'