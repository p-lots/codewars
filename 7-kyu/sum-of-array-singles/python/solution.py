from collections import Counter

def repeats(arr):
    arr_counts = Counter(arr)
    return sum(k for k, v in arr_counts.items() if v == 1)