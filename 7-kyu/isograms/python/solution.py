def is_isogram(strng):
    strng = strng.lower()
    return len(set(strng)) == len(strng)