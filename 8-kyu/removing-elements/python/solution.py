def remove_every_other(my_list):
    return [item for i, item in enumerate(my_list) if i % 2 == 0]
