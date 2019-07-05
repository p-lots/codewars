def make_sieve():
    ret = []
    for i in range(10000):
        ret.append(True)
    ret[0] = False
    ret[1] = False
    for i in range(10000):
        if ret[i]:
            for j in range(i * i, 10000, i):
                ret[j] = False
    return ret

def odd_not_prime(n):
    primes = make_sieve()
    ret = 0
    for i in range(1, n + 1, 2):
        if not primes[i]:
            ret += 1
    return ret