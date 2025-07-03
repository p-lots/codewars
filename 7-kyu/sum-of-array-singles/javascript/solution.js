from collections import Counter

def repeats(arr):
    result = Counter(arr)
    return sum(n for n, _ in result.items() if result[n] == 1)