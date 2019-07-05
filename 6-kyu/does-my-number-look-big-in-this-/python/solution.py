def narcissistic(value):
    value_str = str(value)
    total = 0
    for n in value_str:
        digit = int(n)
        total += pow(digit, len(value_str))
    return total == value