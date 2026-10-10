from itertools import islice, chain

def a_longer(a, b):
    return list(chain.from_iterable(zip(islice(a, len(b)), b))) + a[len(b):]

def b_longer(a, b):
    return list(chain.from_iterable(zip(a, islice(b, len(a))))) + b[len(a):]

def compound_array(a, b):
    return a_longer(a, b) if len(a) > len(b) else b_longer(a, b)
