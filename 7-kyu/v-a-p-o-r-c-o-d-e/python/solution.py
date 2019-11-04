def vaporcode(s):
    return '  '.join(map(lambda l: l.upper(), s.replace(' ', '')))