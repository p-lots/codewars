from preloaded import CHAR_TO_MORSE

def encryption(strng):
    return ' '.join(CHAR_TO_MORSE.get(ch, ' ') for ch in strng)
