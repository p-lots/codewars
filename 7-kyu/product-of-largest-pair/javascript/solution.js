def max_product(a):
    largest = max(a)
    next_largest = min(a)
    for n in a:
        if next_largest < n < largest:
            next_largest = n
    return next_largest * largest
