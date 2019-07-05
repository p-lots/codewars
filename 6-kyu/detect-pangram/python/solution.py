import string

def is_pangram(s):
    counts = {}
    for ch in s.lower():
        if ch in string.ascii_lowercase:
            if ch in counts:
                counts[ch] += 1
            else:
                counts[ch] = 1
    return True if len(counts) == 26 else False