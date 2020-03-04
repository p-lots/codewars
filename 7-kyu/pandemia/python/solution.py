def infected(s):
    s = list(filter(lambda item: len(item) > 0, s.split('X')))
    if not s:
        return 0
    return (float(sum(len(c) for c in s if '1' in c)) / sum(len(c) for c in s)) * 100.0