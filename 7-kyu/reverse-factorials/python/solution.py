def reverse_factorial(num):
    if num == 1:
        return '1!'
    ret = 1
    fac = 1
    while fac < num:
        fac *= ret
        ret += 1
    return f'{ret - 1}!' if fac == num else 'None'
