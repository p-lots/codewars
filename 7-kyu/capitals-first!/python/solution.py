def capitals_first(text):
    capitals = []
    lowers = []
    for word in text.split():
        if word[0].isupper():
            capitals.append(word)
        elif word[0].islower():
            lowers.append(word)
    return ' '.join(capitals + lowers)