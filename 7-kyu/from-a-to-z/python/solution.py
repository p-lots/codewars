from string import ascii_lowercase, ascii_uppercase

def gimme_the_letters(sp):
    first, last = sp.split('-')
    begin = ascii_lowercase.index(first.lower())
    end = ascii_lowercase.index(last.lower()) + 1
    return ''.join(ascii_uppercase[i] if sp[0].isupper() else ascii_lowercase[i] for i in range(begin, end))
