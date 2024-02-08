def disemvowel(strng):
    return ''.join(ch for ch in strng if ch.lower() not in 'aeiou')