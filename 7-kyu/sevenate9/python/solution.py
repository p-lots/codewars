def seven_ate9(str_):
    ret = ''
    for i in range(len(str_) - 1):
        if i == 0:
            ret += str_[i]
            continue
        if str_[i - 1] == '7' and str_[i + 1] == '7' and str_[i] == '9':
            continue
        else:
            ret += str_[i]
    ret += str_[-1]
    return ret