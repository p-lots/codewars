def sort_transform(arr):
    word1 = ''.join([chr(arr[0]), chr(arr[1]), chr(arr[-2]), chr(arr[-1])])
    arr_sorted = sorted(arr)
    word2 = ''.join([chr(arr_sorted[0]), chr(arr_sorted[1]), chr(arr_sorted[-2]), chr(arr_sorted[-1])])
    arr_sorted_rev = sorted(arr, reverse=True)
    word3 = ''.join([chr(arr_sorted_rev[0]), chr(arr_sorted_rev[1]), chr(arr_sorted_rev[-2]), chr(arr_sorted_rev[-1])])
    arr_ascii = sorted([chr(item) for item in arr])
    word4 = ''.join([arr_ascii[0], arr_ascii[1], arr_ascii[-2], arr_ascii[-1]])
    return '-'.join([word1, word2, word3, word4])