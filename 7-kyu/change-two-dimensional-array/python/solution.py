def matrix(array): 
    ret = [n for n in array]
    for i in range(len(ret)):
        if ret[i][i] < 0:
            ret[i][i] = 0
        else:
            ret[i][i] = 1
    return ret
