def odd_one(arr):
    try:
        return [idx for idx, n in enumerate(arr) if n % 2 == 1][0]
    except:
        return -1
