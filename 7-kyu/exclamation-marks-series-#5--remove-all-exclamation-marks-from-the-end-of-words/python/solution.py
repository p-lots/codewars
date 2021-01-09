def remove(s):
    ret = []
    temp_word = ''
    for word in s.split():
        found_letters = False
        for ch in word:
            if ch == '!' and not found_letters:
                temp_word += ch
            elif ch.isalpha():
                found_letters = True
                temp_word += ch
        ret.append(temp_word)
        temp_word = ''
    return ' '.join(ret)
