from string import ascii_lowercase

LOOKUP_TABLE = {ch: str(i) for i, ch in enumerate(ascii_lowercase, 1)}

def encode(strng):
    return ''.join(LOOKUP_TABLE.get(ch, ch) for ch in strng.lower())
