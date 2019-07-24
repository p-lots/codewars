from collections import Counter

def duplicates(arr):
    if len(arr) < 2:
        return 0
    arr_cnt = Counter()
    for n in arr:
        arr_cnt[n] += 1
    return sum(count // 2 for count in arr_cnt.values())