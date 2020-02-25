def absent_vowel(x): 
    lookup = {k: v for k, v in zip(list('aeiou'), list(range(0, 5)))}
    for k, v in lookup.items():
        if k not in x:
            return v