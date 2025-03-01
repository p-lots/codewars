def make_empty(val):
    if val is None:
        return None
    types = {int: 0, float: 0.0, str: "", bool: False, list: [], tuple: (), dict: {}, set: set()}
    for t in types.keys():
        if isinstance(val, t):
            return types.get(t)

def empty_values(lst):
    return [make_empty(elem) for elem in lst]
