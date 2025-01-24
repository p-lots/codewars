def closest(lst):
    if 0 in lst:
        return 0
    smallest_diff = None
    closest_to = lst[0]
    for num in lst:
        curr_diff = abs(0 - num)
        if smallest_diff is None:
            smallest_diff = curr_diff
            closest_to = num
        elif curr_diff < smallest_diff:
            smallest_diff = curr_diff
            closest_to = num
    return closest_to if lst.count(-closest_to) == 0 else None
