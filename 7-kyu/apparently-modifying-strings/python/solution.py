def apparently(strng):
    if not strng:
        return ''
    strng_split = strng.split()
    ret = []
    for i in range(len(strng_split) - 1):
        ret.append(strng_split[i])
        if (ret[-1] == 'and' or ret[-1] == 'but') and strng_split[i + 1] != 'apparently':
            ret.append('apparently')
    ret.append(strng_split[-1])
    if ret[-1] == 'and' or ret[-1] == 'but':
        ret.append('apparently')
    return ' '.join(ret)
            