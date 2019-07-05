def solve(a):
    return sum([1 for item in a if str(item).isdigit() and item % 2 == 0]) - sum([1 for item in a if str(item).isdigit() and item % 2 == 1])