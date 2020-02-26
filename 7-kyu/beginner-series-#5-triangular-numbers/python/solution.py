def is_triangular(t):
    tri_nums = [1]
    n = 2
    while tri_nums[-1] < t:
        tri_nums.append(n * (n + 1) // 2)
        n += 1
    return tri_nums[-1] == t