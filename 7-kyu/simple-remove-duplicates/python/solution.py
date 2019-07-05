def solve(arr): 
    arr_set = set()
    ret = []
    for n in arr[::-1]:
        if n not in arr_set:
            arr_set.add(n)
            ret.append(n)
    return ret[::-1]