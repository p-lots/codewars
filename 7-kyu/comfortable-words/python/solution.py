LEFT_KEYS = 'q, w, e, r, t, a, s, d, f, g, z, x, c, v, b'.split(', ')
RIGHT_KEYS = 'y, u, i, o, p, h, j, k, l, n, m'.split(', ')

def comfortable_word(word):
    if not word:
        return True
    if word[0] in LEFT_KEYS:
        return all(ch in LEFT_KEYS for ch in word[::2]) and all(ch in RIGHT_KEYS for ch in word[1::2])
    else:
        return all(ch in RIGHT_KEYS for ch in word[::2]) and all(ch in LEFT_KEYS for ch in word[1::2])
