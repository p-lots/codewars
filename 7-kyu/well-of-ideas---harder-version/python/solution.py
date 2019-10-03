def well(arr):
    result = sum(1 for subarr in arr for item in subarr if type(item) == str and item.lower() == 'good')
    return 'I smell a series!' if result > 2 else 'Publish!' if result else 'Fail!'
    