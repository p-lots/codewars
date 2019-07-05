def tidyNumber(n):
    n_list = [int(digit) for digit in str(n)]
    for i in range(len(n_list) - 1):
        if n_list[i + 1] < n_list[i]:
            return False
    return True