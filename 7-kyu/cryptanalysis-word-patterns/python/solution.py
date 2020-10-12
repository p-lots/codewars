def word_pattern(word):
    seen_letters = {}
    curr = 0
    ret = []
    for letter in word.lower():
        if letter not in seen_letters:
            seen_letters[letter] = curr
            curr += 1
        ret.append(seen_letters[letter])
    return '.'.join(str(elem) for elem in ret)