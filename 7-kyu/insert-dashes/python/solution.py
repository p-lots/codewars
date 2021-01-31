def insert_dash(num):
    num_lst = list(str(num))
    ret = ''
    while num_lst:
        if ret and int(ret[-1]) % 2 == 1 and int(num_lst[0]) % 2 == 1:
            ret += '-'
        ret += num_lst[0]
        num_lst.pop(0)
    return ret