def iq_test(numbers):
    nums_int = [int(n) for n in numbers.split()]
    mod_two = [n % 2 for n in nums_int]
    zero_count = mod_two.count(0)
    one_count = mod_two.count(1)
    if zero_count > one_count:
        idx = mod_two.index(1)
        return idx + 1
    else:
        idx = mod_two.index(0)
        return idx + 1