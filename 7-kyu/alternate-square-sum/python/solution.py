def alternate_sq_sum(arr):
    return sum([elem if i % 2 == 0 else elem * elem for i, elem in enumerate(arr)])
