def binary_cleaner(seq): 
    return ([n for n in seq if 0 <= n < 2], [i for i in range(len(seq)) if seq[i] > 1])