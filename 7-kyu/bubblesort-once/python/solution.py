def bubblesort_once(l):
    lst = l[:]
    i = 0
    while i < len(lst) - 1:
        if (lst[i + 1] < lst[i]):
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
        i += 1
    return lst