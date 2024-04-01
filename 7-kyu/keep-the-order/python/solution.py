def keep_order(ary, val):
    for idx, num in enumerate(ary):
        if num >= val:
            return idx
    return len(ary)