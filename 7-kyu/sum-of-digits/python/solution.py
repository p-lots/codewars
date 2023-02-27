def sum_of_digits(digits): 
    if digits is None:
        return ''
    elif type(digits) == int:
        digits = str(digits)
    return f'{" + ".join(digit for digit in digits)} = {sum(map(int, digits))}'
