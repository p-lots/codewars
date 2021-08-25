def gordon(a):
    return ' '.join(f'{word.translate(word.maketrans("aeiou", "@****")).upper()}!!!!' for word in a.lower().split())
