from functools import reduce
from operator import mul

def geo_mean(nums, arith_mean):
    arith_total = arith_mean * (len(nums) + 1)
    list_total = sum(nums)
    nums.append(arith_total - list_total)
    return reduce(mul, nums) ** (1 / len(nums))
