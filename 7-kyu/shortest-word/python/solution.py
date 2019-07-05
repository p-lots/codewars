def find_short(s):
    arr = [word for word in s.split()]
    return len(sorted(arr, key=len)[0])