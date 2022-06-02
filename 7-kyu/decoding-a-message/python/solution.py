from string import ascii_lowercase

def decode(message):
    LOOKUP = {k: v for k, v in zip(ascii_lowercase, ascii_lowercase[::-1])}
    return ''.join(LOOKUP.get(ch, ch) for ch in message)
