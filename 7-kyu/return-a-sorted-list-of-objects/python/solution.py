def sort_list(sort_by, lst):
    return sorted(lst, key=lambda elem: elem.get(sort_by), reverse=True)
