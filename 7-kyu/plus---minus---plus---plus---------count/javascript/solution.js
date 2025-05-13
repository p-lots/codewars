def catch_sign_change(lst):
    if not lst:
        return 0
    prev_was_positive = lst[0] > 0
    ret = 0
    for i in range(1, len(lst)):
        if lst[i] < 0 and prev_was_positive:
            ret += 1
            prev_was_positive = False
        elif lst[i] >= 0 and not prev_was_positive:
            ret += 1
            prev_was_positive = True
    return ret