def missing_values(seq): 
    x = 0
    y = 0
    for elem in seq:
        if seq.count(elem) == 2:
            y = elem
        elif seq.count(elem) == 1:
            x = elem
    return x * x * y
