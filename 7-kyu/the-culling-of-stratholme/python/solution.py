import re

def purify(s: str) -> str:
    purified = []
    for word in s.split():
        pure_word = re.sub(r'[^i]?i[^i]?', '', word, 0, re.IGNORECASE)
        if pure_word:
            purified.append(pure_word)
    return ' '.join(purified)
