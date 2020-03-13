from functools import reduce

def super_size(n):
    n = sorted(map(int, str(n)), reverse=True)
    return reduce(lambda acc, curr: acc * 10 + curr, n)