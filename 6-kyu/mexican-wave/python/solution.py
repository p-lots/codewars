def wave(word):
    ret = []
    for i in range(len(word)):
        if not word[i].isalpha():
            continue
        if i == 0:
            ret.append(word[i].upper() + word[i+1:])
        elif i < len(word) - 1:
            ret.append(word[:i] + word[i].upper() + word[i + 1:])
        else:
            ret.append(word[:i] + word[i].upper())
    return ret