def largestPower(N):
    k = -1
    while 3 ** k < N:
        k += 1
    return k - 1