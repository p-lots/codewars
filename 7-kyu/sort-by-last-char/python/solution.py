def last(s):
    s_split = s.split()
    return list(sorted(s_split, key=lambda word: (word[-1], s_split.index(word))))