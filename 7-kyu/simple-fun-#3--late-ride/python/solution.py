def late_ride(n):
    hours = n // 60
    minutes = n % 60
    return sum([int(digit) for digit in str(hours)]) + sum([int(digit) for digit in str(minutes)])