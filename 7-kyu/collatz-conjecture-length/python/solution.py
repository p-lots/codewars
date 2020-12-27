def collatz(n):
    ret = 0
    while n != 1:
        n = n * 3 + 1 if n % 2 == 1 else n // 2
        ret += 1
    return ret + 1
