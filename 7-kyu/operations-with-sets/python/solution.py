def process_2arrays(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    return[len(set1 & set2), len(set1 ^ set2), len(set1 - set2), len(set2 - set1)]