def trim(phrase, size):
    if len(phrase) <= size:
        return phrase
    elif len(phrase) <= 3 or size <= 3:
        return phrase[:size] + '...'
    return phrase[:size - 3] + '...'
