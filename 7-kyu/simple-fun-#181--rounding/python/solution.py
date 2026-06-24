def rounding(n,m):
    if n % m == m / 2:
        return n
    return m * round(n / m)
