def make_model_year(lst):
    ret = {}
    for elem in lst:
        if isinstance(elem, str):
            ret['make'] = elem
        elif isinstance(elem, tuple):
            ret['model'] = f'{elem[0]} {elem[1]}'
        elif isinstance(elem, bool):
            ret['new'] = elem
        elif isinstance(elem, int):
            ret['year'] = elem
    return ret