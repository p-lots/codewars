def validate(n):
    n_arr = [int(digit) for digit in str(n)]
    for i in range(len(n_arr) - 2, -1, -2):
        n_arr[i] *= 2
        if n_arr[i] > 9:
            n_arr[i] -= 9
    return sum(n_arr) % 10 == 0