def create_array_of_tiers(n):
    n = str(n)
    return [n[:i] for i in range(1, len(n) + 1)]
