lookup = {letter: str(num) for letter, num in zip(['a', 'e', 'i', 'o', 'u'], range(1, 6))}
rev_lookup = {v: k for k, v in lookup.items()}

def encode(st):
    return ''.join(lookup.get(ch, ch) for ch in st)
    
def decode(st):
    return ''.join(rev_lookup.get(ch, ch) for ch in st)