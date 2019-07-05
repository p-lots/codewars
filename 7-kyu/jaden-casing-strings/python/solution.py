def toJadenCase(strng):
    return ' '.join(word[0].upper() + word[1:] for word in strng.split())