from itertools import combinations

def digits(n):
    return [sum(map(int, pair)) for pair in combinations(str(n), 2)]