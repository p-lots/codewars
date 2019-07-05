def is_valid_string(words):
    for letter in words:
        if letter in 'GHIJKLMNPQRTUVWXYZ':
            return False
    return True

def hex_word_sum(s):
    if not s:
        return 0
    ret = 0
    s = s.replace('S', '5').replace('O', '0')
    for word in s.split():
        if not is_valid_string(word):
            continue
        ret += int(word, 16)
    return ret