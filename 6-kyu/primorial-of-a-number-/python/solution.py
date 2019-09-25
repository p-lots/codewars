def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    elif x % 2 == 0:
        return False
    for j in range(3, x + 1, 2):
        if x % j == 0 and x != j:
            return False
    return True

def num_primorial(n):
    prime_count = 1
    ret = 1
    i = 0
    while prime_count <= n:
        if is_prime(i):
            ret *= i
            prime_count += 1
        i += 1
    return ret