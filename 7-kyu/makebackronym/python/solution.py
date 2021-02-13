#preloaded variable: "dictionary"

def make_backronym(acronym):
    return ' '.join(dictionary[ch.upper()] for ch in acronym)
