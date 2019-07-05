def explode(arr):  
    if type(arr[0]) is int and type(arr[1]) is int:
        score = arr[0] + arr[1]
    elif type(arr[0]) is int or type(arr[1]) is int:
        score = arr[0] if type(arr[0]) is int else arr[1]
    else:
        return 'Void!'
    ret = []
    for n in range(score):
        ret.append(arr)
    return ret