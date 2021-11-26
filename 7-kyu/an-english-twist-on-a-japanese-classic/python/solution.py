def game(words):
    if not words:
        return []
    ret = []
    if len(words[0]) > 0:
        ret.append(words[0])
        prev = words[0][-1]
    for word in words[1:]:
        if len(word) == 0:
            break
        if word[0] == prev:
            ret.append(word)
        else:
            break
        prev = word[-1]
    return ret
