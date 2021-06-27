def alan(arr):
    to_find = ['Rejection', 'Disappointment', 'Backstabbing Central', 'Shattered Dreams Parkway']
    for stop in arr:
        if stop in to_find:
            idx = to_find.index(stop)
            del to_find[idx]
    return 'Smell my cheese you mother!' if len(to_find) == 0 else 'No, seriously, run. You will miss it.'
