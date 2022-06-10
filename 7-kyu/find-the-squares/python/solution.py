def find_squares(num):
    for i in range(1, 10000000):
        i_sq = i ** 2
        j_sq = (i + 1) ** 2
        if j_sq - i_sq == num:
            return f'{j_sq}-{i_sq}'