def encode_tuple(strng):
    count = 1
    prev = strng[0]
    ret = []
    for i in range(1, len(strng)):
        if strng[i] == prev:
            count += 1
        else:
            to_append = (prev, count)
            ret.append(to_append)
            count = 1
            prev = strng[i]
    ret.append((prev, count))
    return ret

def encode(strng):
    return ''.join('{0}{1}'.format(count, ch) for (ch, count) in encode_tuple(strng))
    
def decode(strng): 
    i = 0
    ret = []
    count_str = ''
    while i < len(strng):
        if strng[i].isdigit():
            count_str += strng[i]
        elif strng[i].isalpha():
            if not count_str:
                count_str = '1'
            for n in range(int(count_str)):
                ret.append(strng[i])
            count_str = ''
        i += 1
    return ''.join(ret)