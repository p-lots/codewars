def get_average(lst): 
    return round(sum(elem['age'] for elem in lst) / len(lst))
