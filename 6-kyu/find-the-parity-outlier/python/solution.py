def find_outlier(integers):
    no_evens = filter(lambda item: item % 2 == 0, integers)
    if len(no_evens) == 1: return no_evens[0]
    no_odds = filter(lambda item: item % 2 == 1, integers)
    return no_odds[0]