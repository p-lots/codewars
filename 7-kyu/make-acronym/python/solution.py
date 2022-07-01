def to_acronym(inp):
    return ''.join(word[0].upper() for word in inp.split(' '))
