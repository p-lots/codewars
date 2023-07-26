from string import ascii_lowercase as alphabet

def encode(strng):
    return ''.join(str(alphabet.index(ch.lower()) % 2) if ch.isalpha() else ch for ch in strng)
