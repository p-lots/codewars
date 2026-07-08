def spot_diff(s1, s2):
    return [idx for idx, (ch1, ch2) in enumerate(zip(s1, s2)) if ch1 != ch2]
