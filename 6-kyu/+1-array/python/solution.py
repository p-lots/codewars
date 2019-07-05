def up_array(arr):
    if not arr:
        return None
    num = 0
    for n in arr:
        if n < 0 or n > 9:
            return None
        num = num * 10 + n
    num += 1
    ret = []
    while num > 0:
        ret.append(num % 10)
        num = num // 10
    return list(reversed(ret))