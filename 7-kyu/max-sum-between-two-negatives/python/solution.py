def split_by_neg(arr):
    ret = []
    temp = []
    found_first_neg = False
    for n in arr:
        if n < 0:
            found_first_neg = True
            if temp:
                ret.append(temp)
                temp = []
        elif n > 0 and found_first_neg:
            temp.append(n)
    return ret

def max_sum_between_two_negatives(arr):
    arr_split = [sum(subarr) for subarr in split_by_neg(arr)]
    return max(arr_split, default=0) if len(list(filter(lambda n: n < 0, arr))) > 1 else -1
