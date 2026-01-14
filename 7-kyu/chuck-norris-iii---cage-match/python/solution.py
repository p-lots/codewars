def head_smash(arr):
    if isinstance(arr, list) or isinstance(arr, str):
        if len(arr) == 0:
            return 'Gym is empty'
        return [line.replace('O', ' ' ) for line in arr]
    return 'This isn\'t the gym!!'
