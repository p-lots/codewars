def solve(s):
    upper = sum(1 for ch in s if ch.isupper())
    lower = sum(1 for ch in s if ch.islower())
    nums = sum(1 for ch in s if ch.isdigit())
    specials = len(s) - upper - lower - nums
    return [upper, lower, nums, specials]