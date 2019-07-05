def alpha_seq(string):
    return ','.join(ch.upper() + ''.join([ch for c in range(ord(ch) - ord('a'))]) for ch in sorted(list(string.lower())))