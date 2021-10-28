def word_to_bin(word):
    return [f'{ord(ch):b}'.zfill(8) for ch in word]
