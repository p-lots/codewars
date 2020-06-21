from collections import Counter

def string_letter_count(s):
    s = sorted([ch for ch in s.lower() if ch.isalpha()])
    s_counts = Counter(s)
    return ''.join(f"{v}{k}" for k, v in s_counts.items())