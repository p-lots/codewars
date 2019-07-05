def decode(code, key):
    key_str = str(key)
    return ''.join([chr(96 + letter - int(key_str[i % len(key_str)])) for (i, letter) in enumerate(code)])