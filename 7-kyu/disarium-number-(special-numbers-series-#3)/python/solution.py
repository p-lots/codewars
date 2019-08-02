def disarium_number(number):
    number_lst = list(map(int, str(number)))
    ret = sum(n ** (i + 1) for i, n in enumerate(number_lst))
    return 'Disarium !!' if ret == number else 'Not !!'