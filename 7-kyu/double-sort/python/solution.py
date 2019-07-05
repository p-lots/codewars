def db_sort(arr): 
    return sorted([item for item in arr if type(item) == int]) + sorted([item for item in arr if type(item) == str])