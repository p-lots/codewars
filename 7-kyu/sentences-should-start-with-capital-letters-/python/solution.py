def fix(paragraph):
    if not paragraph:
        return ''
    return '. '.join(sentence[0][0].upper() + sentence[0][1:] + sentence[1:] for sentence in paragraph.split('. '))
