def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3 or n == 5:
        return True
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def next_prime(n):
    if is_prime(n):
        n += 1
    while not is_prime(n):
        n += 1
    return n
