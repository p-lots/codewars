def determine_sequence(series_array):
    if all(n == 0 for n in series_array):
        return 0
    diffs = [y - x for x, y in zip(series_array, series_array[1:])]
    is_AP = all(x == y for x, y in zip(diffs, diffs[1:]))
    if all(n != 0 for n in series_array):
        ratios = [y / x for x, y in zip(series_array, series_array[1:])]
        is_GP = all(x == y for x, y in zip(ratios, ratios[1:]))
    else:
        is_GP = False
    return 2 if is_AP and is_GP else 1 if is_GP else 0 if is_AP else -1
