def sum_square_even_root_odd(nums):
    return round(sum(n ** 2 for n in nums if n % 2 == 0) + sum(n ** 0.5 for n in nums if n % 2 == 1), 2)
