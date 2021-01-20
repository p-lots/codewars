def two_decimal_places(number):
    number = str(number)
    dec_idx = number.index('.')
    return float(number[:dec_idx + 3])