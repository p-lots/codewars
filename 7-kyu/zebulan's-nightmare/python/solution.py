def zebulans_nightmare(function):
    return ''.join(word[0].upper() + word[1:] if i > 0 else word for i, word in enumerate(function.split('_')))
