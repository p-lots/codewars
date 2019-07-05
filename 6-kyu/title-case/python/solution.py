def title_case(title, minor_words=None):
    if not minor_words:
        return ' '.join(word.capitalize() for word in title.split())
    minor_words = minor_words.lower().split()
    ret = []
    arr = title.lower().split()
    for word in arr:
        if word in minor_words and word is not arr[0]:
            ret.append(word)
        else:
            ret.append(word.capitalize())
    return ' '.join(ret)