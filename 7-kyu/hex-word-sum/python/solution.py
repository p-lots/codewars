def hex_word_sum(strng):
    strng = strng.replace('S', '5').replace('O', '0')
    return sum(int(word, 16) if all(letter in '0123456789ABCDEF' for letter in word) else 0 for word in strng.split())