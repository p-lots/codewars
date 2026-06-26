from string import ascii_lowercase as alphabet

def closed_bracket_word(st):
    counterparts = {ch: alphabet[len(alphabet) - idx - 1] for idx, ch in enumerate(alphabet)}
    return all(st[len(st) - idx - 1] == counterparts[ch] for idx, ch in enumerate(st))
