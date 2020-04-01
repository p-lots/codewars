def max_product(lst, n_largest_elements):
    lst = sorted(lst)
    ret, count = 1, 0
    while count < n_largest_elements:
        if lst:
            ret *= lst[-1]
            lst.pop()
        count += 1
    return ret