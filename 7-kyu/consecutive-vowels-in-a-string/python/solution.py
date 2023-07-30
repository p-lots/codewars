def get_the_vowels(word):
    vowels = 'aeiou'
    vowels_idx = 0
    for ch in word:
        if ch == vowels[vowels_idx % len(vowels)]:
            vowels_idx += 1
    return vowels_idx
