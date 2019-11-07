def find_average(nums):
    if not nums:
        return 0
    return float(sum(nums)) / len(nums)