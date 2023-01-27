def remove_duplicate_words(s):
    if not s:
        return ''
    s_split = s.split()
    s_set = []
    ret = []
    for word in s_split:
        if word not in s_set:
            s_set.append(word)
            ret.append(word)
    return ' '.join(ret)