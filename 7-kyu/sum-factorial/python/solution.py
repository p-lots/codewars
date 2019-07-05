from functools import reduce

def do_factorial(n):
    return reduce(lambda accum, n: accum * n, [i for i in range(1, n + 1)])

def sum_factorial(lst):
    return sum(do_factorial(n) for n in lst)