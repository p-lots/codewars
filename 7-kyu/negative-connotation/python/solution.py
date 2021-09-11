def connotation(strng):
    return sum(1 if ord('a') <= ord(word[0]) <= ord('m') else -1 for word in strng.lower().split()) >= 0
