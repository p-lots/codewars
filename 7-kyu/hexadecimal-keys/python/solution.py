from math import floor, sqrt

def find_prime_factors(n):
    ret = []
    while n % 2 == 0:
        n /= 2
    for i in range(3, floor(sqrt(n)) + 1, 2):
        while n % i == 0:
            ret.append(i)
            n /= i
    if n > 2:
        ret.append(n)
    return ret

def find_key(encryption_key):
    prime_factors = find_prime_factors(int(encryption_key, 16))
    return (prime_factors[-1] - 1) * (prime_factors[-2] - 1)