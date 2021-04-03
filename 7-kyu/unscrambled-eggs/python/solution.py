def unscramble_eggs(word):
    return ''.join(w for w in word.split('egg') if len(w) > 0)
