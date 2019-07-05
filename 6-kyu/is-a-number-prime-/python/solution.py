from math import sqrt

def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    i = 3
    while i <= sqrt(num):
        if num % i == 0:
            return False
        i += 2
    return True