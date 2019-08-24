def even_numbers(arr, n):
    arr_even = list(filter(lambda item: item % 2 == 0, arr))
    ret = []
    count = 0
    for i in reversed(arr_even):
        if count < n:
            ret.append(i)
        count += 1
    return list(reversed(ret))