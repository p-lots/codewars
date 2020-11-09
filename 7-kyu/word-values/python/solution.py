def name_value(my_list):
    return [sum(ord(ch) - ord('a') + 1 for ch in elem.replace(' ', '')) * i for i, elem in enumerate(my_list, 1)]