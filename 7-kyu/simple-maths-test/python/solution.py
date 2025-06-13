def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def number_property(n):
    prime = is_prime(n)
    even = n % 2 == 0
    ten = n % 10 == 0
    return [prime, even, ten]