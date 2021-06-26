def buy(x, arr):        
    if len(arr) < 2 or sum(arr) < x:
        return None
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j and arr[i] + arr[j] == x:
                return [i, j]
