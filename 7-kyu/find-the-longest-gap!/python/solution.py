def gap(num):
    num_bin = bin(num)[2:]
    i = 0
    ret = 0
    while i < len(num_bin):
        if num_bin[i] == '1':
            i += 1
            curr_count = 0
            while i < len(num_bin) and num_bin[i] == '0':
                curr_count += 1
                i += 1
                if i < len(num_bin) and num_bin[i] == '1':
                    ret = max(curr_count, ret)
        else:
            i += 1
    return ret