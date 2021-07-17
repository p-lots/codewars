def count_developers(lst):
    return len([dct for dct in lst if dct['language'] == 'JavaScript' and dct['continent'] == 'Europe'])
