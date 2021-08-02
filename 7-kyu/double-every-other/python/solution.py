def double_every_other(lst):
    return [elem * 2 if i % 2 == 1 else elem for i, elem in enumerate(lst)]
