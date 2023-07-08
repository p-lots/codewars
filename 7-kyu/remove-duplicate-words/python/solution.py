def remove_duplicate_words(s):
    if not s:
        return ''
    ret = []
    for word in s.split():
        if word not in ret:
            ret.append(word)
    return ' '.join(ret)