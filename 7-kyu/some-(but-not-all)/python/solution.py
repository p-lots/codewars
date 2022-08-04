def some_but_not_all(seq, pred): 
    return any(pred(elem) for elem in seq) and not all(pred(elem) for elem in seq)