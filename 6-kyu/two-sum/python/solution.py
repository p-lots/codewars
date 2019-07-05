def two_sum(numbers, target):
    for i, n in enumerate(numbers):
        for j, m in enumerate(numbers):
            if n + m == target and i != j:
                return [i, j]