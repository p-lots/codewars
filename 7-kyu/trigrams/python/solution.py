def trigrams(phrase):
    # Good Luck!
    if len(phrase) < 3:
        return ''
    phrase = phrase.replace(' ', '_')
    return ' '.join(phrase[i:i + 3] for i in range(len(phrase) - 2))