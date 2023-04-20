_all = all

def all(seq, fun): 
    return _all(fun(elem) for elem in seq)
