def rank_of_element(arr, i):
    return sum(el <= arr[i] for el in arr[:i]) + sum(el < arr[i] for el in arr[i:])
