def pathfinder_scores(scores):
    if not all(7 <= n <= 18 for n in scores):
        return False
    lookup = {7: -4, 8: -2, 9: -1, 10: 0, 11: 1, 12: 2, 13: 3, 14: 5, 15: 7, 16: 10, 17: 13, 18: 17}
    return sum(lookup[n] for n in scores) <= 25