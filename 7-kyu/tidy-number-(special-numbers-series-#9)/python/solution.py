def tidyNumber(n):
    n_list = [int(digit) for digit in str(n)]
    return all(i <= j for i, j in zip(n_list, n_list[1:]))