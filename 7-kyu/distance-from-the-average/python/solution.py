def distances_from_average(test_list):
    avg = sum(test_list) / len(test_list)
    return [round(avg - n, 2) for n in test_list]
