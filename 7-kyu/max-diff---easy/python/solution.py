def max_diff(lst):
    if len(lst) < 2:
        return 0
    lst = sorted(lst)
    return lst[-1] - lst[0]