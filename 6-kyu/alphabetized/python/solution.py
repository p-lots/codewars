def alphabetized(s):
    if not s:
        return s
    s_only_letters = ''.join([ch for ch in s if ch.isalpha()])
    if not s_only_letters:
        return s_only_letters
    s_sorted = sorted(s_only_letters, key=lambda ch: ch.lower())
    return ''.join(s_sorted)