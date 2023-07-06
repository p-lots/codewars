from collections import Counter

def highest_rank(arr):
    arr_counts = Counter(arr)
    return max(arr, key=lambda elem: (arr_counts.get(elem), elem))
