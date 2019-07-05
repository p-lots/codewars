def reverse_words(text):
    ret = ''
    i = 0
    while i < len(text):
        if text[i].isspace():
            spc = ''
            while i < len(text) and text[i].isspace():
                spc += text[i]
                i += 1
            ret += spc
        else:
            wrd = ''
            while i < len(text) and not text[i].isspace():
                wrd += text[i]
                i += 1
            wrd = wrd[::-1]
            ret += wrd
    return ret