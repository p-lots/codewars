def gimme(input_array):
    arr_min, arr_max = min(input_array), max(input_array)
    for i, n in enumerate(input_array):
        if n != arr_min and n != arr_max:
            return i