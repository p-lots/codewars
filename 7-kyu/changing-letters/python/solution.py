def swap(st):
    return ''.join(l.upper() if l in 'aeiou' else l for l in st)