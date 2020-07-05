def divisors(integer):
    ret = [n for n in range(2, integer) if integer % n == 0]
    return ret or f'{integer} is prime'