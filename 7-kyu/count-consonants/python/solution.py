def consonant_count(s):
    return sum(ch not in 'aeiou' and ch.isalpha() for ch in s.lower())
