from functools import reduce
from operator import mul

def factorial(n):
    if n == 0: return 1
    if n <= 2: return n
    ret = reduce(mul, range(1, n + 1))
    return ret

def strong_num(number):
    number_lst = list(map(int, str(number)))
    fac_sum = sum(map(factorial, number_lst))
    return 'STRONG!!!!' if fac_sum == number else 'Not Strong !!'