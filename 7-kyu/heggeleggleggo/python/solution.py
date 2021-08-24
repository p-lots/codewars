def heggeleggleggo(word):
    ret = ''
    for ch in word:
        ret += ch
        if ch.lower() not in 'aeiou ':
            ret += 'egg'
    return ret
