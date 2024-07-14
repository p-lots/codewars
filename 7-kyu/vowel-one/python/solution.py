def vowel_one(s):
    return ''.join('1' if ch.lower() in 'aeiou' else '0' for ch in s)
