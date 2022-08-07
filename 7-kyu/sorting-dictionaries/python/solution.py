def sort_dict(d):
    """return a sorted list of tuples from the dictionary"""
    return sorted([(k, v) for k, v in d.items()], key=lambda elem: elem[1], reverse=True)