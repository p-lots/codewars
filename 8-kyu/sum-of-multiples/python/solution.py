def sum_mul(n, m):
    if m <= 0 or n <= 0:
        return 'INVALID'
    try:
        return sum(x for x in range(n, m, n))
    except:
        return 'INVALID'