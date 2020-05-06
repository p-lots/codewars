def letter_check(arr): 
    return all(ch in arr[0].lower() for ch in arr[1].lower())