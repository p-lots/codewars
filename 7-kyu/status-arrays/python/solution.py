from collections import Counter

def status(nums):
    cnt = Counter(nums)
    status_arr = [i + sum(v for k, v in cnt.items() if k < n) for i, n in enumerate(nums)]
    nums_zipped = zip(nums, status_arr)
    return [elem[0] for elem in sorted(nums_zipped, key=lambda p: p[1])]