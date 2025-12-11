def contain_all_rots(strng, arr):
    for i in range(len(strng)):
        rot = strng[i:] + strng[:i]
        if arr.count(rot) == 0:
            return False
    return True
