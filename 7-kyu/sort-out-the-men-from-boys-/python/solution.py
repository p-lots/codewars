def men_from_boys(arr):
    evens = list(set([n for n in arr if n % 2 == 0]))
    odds = list(set([n for n in arr if n % 2 == 1]))
    return sorted(evens) + sorted(odds, reverse=True)