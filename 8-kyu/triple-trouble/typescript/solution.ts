def triple_trouble(one, two, three):
    ret = ''
    for i in range(len(one)):
        ret += one[i] + two[i] + three[i]
    return ret