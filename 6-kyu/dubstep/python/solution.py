def song_decoder(song):
    i = 0
    word_temp = ''
    ret = []
    while i < len(song):
        if song[i:i + 3] == "WUB":
            if len(word_temp) > 0:
                ret.append(word_temp)
                word_temp = ''
            i += 3
        else:
            word_temp += song[i]
            i += 1
    if len(word_temp) > 0:
        ret.append(word_temp)
    return ' '.join(ret)