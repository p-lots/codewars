def to_weird_case(strng):
    return ' '.join(''.join(ch.upper() if i % 2 == 0 else ch.lower() for i, ch in enumerate(word)) for word in strng.split())