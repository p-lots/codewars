def balanced_num(number):
    number_str = str(number)
    if len(number_str) <= 2:
        return 'Balanced'
    middle = len(number_str) // 2
    if len(number_str) % 2 == 0: middle -= 1
    lhs = list(map(int, number_str[:middle]))
    rhs = list(map(int, number_str[len(number_str) - middle:]))
    return 'Balanced' if sum(lhs) == sum(rhs) else 'Not Balanced'