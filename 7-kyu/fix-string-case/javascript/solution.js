def solve(s):
    upper_count = sum(1 for ch in s if ch.isupper())
    lower_count = sum(1 for ch in s if ch.islower())
    return s.upper() if upper_count > lower_count else s.lower()