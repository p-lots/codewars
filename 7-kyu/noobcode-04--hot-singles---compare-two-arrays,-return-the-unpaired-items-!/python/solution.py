def hot_singles(arr1, arr2):
    set1 = set(arr1)
    set2 = set1.symmetric_difference(set(arr2))
    arrs = arr1 + arr2
    return sorted(list(set2), key=lambda elem: arrs.index(elem))
