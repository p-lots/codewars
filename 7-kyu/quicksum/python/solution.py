def quicksum(packet):
    ret = 0
    for i, item in enumerate(packet):
        if item not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ ':
            return 0
        elif item.isalpha():
            ret += (i + 1) * (ord(item) - ord('A') + 1)
    return ret
