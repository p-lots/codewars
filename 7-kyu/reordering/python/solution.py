def re_ordering(text):
    return ' '.join(sorted(text.split(), key=lambda item: False if item[0].isupper() else True))