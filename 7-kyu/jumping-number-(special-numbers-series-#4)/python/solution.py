def jumping_number(number):
    number_lst = list(map(int, str(number)))
    number_zip = zip(number_lst, number_lst[1:])
    return 'Jumping!!' if all(abs(item[0] - item[1]) == 1 for item in number_zip) else 'Not!!'