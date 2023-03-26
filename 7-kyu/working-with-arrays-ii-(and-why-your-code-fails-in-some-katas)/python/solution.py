def remove_nth_element(lst, n):
    return [el for i, el in enumerate(lst) if i != n]
