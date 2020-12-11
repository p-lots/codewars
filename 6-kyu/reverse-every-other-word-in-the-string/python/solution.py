def reverse_alternate(strng):
    if not strng:
        return ''
    strng_split = strng.strip().split()
    return ' '.join(word[::-1] if i % 2 == 1 else word for i, word in enumerate(strng_split))
