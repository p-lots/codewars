def incrementer(nums):
    return [(n + i + 1) % 10 for i, n in enumerate(nums)]