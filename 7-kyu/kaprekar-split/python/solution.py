def kaprekar_split(n):
    if n == 1:
        return 0
    n_sq = n * n
    n_sq_str = str(n_sq)
    if len(n_sq_str) == 2:
        if int(n_sq_str[0]) + int(n_sq_str[1]) == n:
            return 1
    for i in range(1, len(n_sq_str) - 1):
        if int(n_sq_str[:i]) + int(n_sq_str[i:]) == n:
            return i
    return -1
