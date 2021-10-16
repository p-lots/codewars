def vowel_2_index(strng):
    return ''.join(ch if ch.lower() not in 'aeiou' else str(i) for i, ch in enumerate(strng, 1))