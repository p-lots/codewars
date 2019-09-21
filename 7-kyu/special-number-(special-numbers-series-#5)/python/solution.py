def special_number(number):
    return 'Special!!' if all(digit < 6 for digit in map(int, str(number))) else 'NOT!!'