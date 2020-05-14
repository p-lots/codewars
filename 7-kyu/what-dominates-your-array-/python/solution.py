from collections import Counter

def dominator(arr):
    if not arr:
        return -1
    counts = Counter(arr)
    for key, val in counts.items():
        if val > len(arr) // 2:
            return key
    return -1