def replace_exclamation(s):
    return ''.join('!' if ch.lower() in 'aeiou' else ch for ch in s)
