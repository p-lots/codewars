from functools import reduce

def reverse(n):
    digits = []
    while n > 0:
        digits.append(n % 10)
        n //= 10
    return reduce((lambda acc, add: acc * 10 + add), digits)