def duplicates(array):
    ret = []
    seen_items = []
    for item in array:
        if item not in seen_items:
            seen_items.append(item)
        elif array.count(item) > 1 and item not in ret:
            ret.append(item)
    return ret