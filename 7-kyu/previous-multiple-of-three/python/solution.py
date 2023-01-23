def prev_mult_of_three(n):
    n = str(n)
    while n:
        if int(n) % 3 == 0:
            return int(n)
        n = n[:-1]
    return None
