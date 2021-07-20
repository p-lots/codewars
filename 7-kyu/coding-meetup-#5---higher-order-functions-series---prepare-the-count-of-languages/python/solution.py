def count_languages(lst): 
    ret = {}
    for elem in lst:
        lang = elem['language']
        if lang not in ret:
            ret[lang] = 1
        else:
            ret[lang] += 1
    return ret
