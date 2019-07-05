def duplicate_encode(word):
    ret = ''
    word = word.lower()
    for ch in word:
        if word.count(ch) == 1:
            ret += '('
        else:
            ret += ')'
    return ret