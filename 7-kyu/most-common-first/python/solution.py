def most_common(s):
    return ''.join(sorted(s, key=lambda ch: -s.count(ch)))