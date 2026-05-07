def pair_zeros(arr):
    arry = []
    cnt = 0
    for n in arr:
        if n == 0:
            cnt += 1
            if cnt % 2 == 1:
                arry.append(n)
        else:
            arry.append(n)
    return arry
