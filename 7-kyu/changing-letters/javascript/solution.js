def is_vowel(letter):
    letter = letter.lower()
    return letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u'

def swap(st):
    return ''.join(l.upper() if is_vowel(l) else l for l in st)