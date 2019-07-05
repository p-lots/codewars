def dig_pow(number, power):
    num_arr = [int(digit) for digit in str(number)]
    total = 0
    for digit in num_arr:
        total += digit ** power
        power += 1
    return total / number if total % number == 0 else -1