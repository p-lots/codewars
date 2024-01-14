def char_to_ascii(s):
    return {ch: ord(ch) for ch in set([c for c in s if c.isalpha()])} if s else None
