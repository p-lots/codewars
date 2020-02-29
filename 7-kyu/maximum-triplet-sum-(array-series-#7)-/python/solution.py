def max_tri_sum(numbers):
    numbers = sorted(list(set(numbers)), reverse=True)
    return sum(numbers[:3])
    