def func(n):
    return n % 2 == 0

def map(arr, somefunction):
    if not callable(somefunction):
        return 'given argument is not a function'
    try:
        arr = [int(n) for n in arr]
        return [somefunction(n) for n in arr]
    except:
        return 'array should contain only numbers'