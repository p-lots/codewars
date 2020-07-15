def multiply_and_filter(seq, multiplier): 
    return list(map(lambda n: n * multiplier, filter(lambda item: (isinstance(item, int) or isinstance(item, float)) and not isinstance(item, bool), seq)))