def sum_of_n(n):
    return [(sum(range(number + 1))) * (-1 if n < 0 else 1) for number in range(abs(n) + 1)]