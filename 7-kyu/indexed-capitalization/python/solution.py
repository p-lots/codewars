def capitalize(s, ind):
    s = list(s)
    for idx in ind:
        if idx >= len(s):
            continue
        s[idx] = s[idx].upper()
    return ''.join(s)