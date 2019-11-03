def first_non_repeated(s):
    for ch in s:
        if s.count(ch) == 1:
            return ch
    return None