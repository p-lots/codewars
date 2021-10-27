def who_took_the_car_key(message):
    return ''.join(chr(int(letter, 2)) for letter in message)
