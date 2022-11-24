def divisors(n):
    if n < 1: return 0
    elif n == 1: return 1
    count = 2
    for i in range(2, n):
        if n % i == 0:
            count += 1
    return count