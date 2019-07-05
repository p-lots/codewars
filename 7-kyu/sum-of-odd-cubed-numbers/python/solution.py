def cube_odd(arr):
    for item in arr:
        if type(item) != int:
            return None
    return sum(n ** 3 for n in arr if (n ** 3) % 2 == 1)