def copy_list(l):
    if type(l) == list:
        return [elem for elem in l]
    raise ValueError
