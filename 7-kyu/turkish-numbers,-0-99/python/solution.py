def get_turkish_number(num):
    ones_lookup_table = {0: 'sıfır', 1: 'bir', 2: 'iki', 3: 'üç', 4: 'dört',
        5: 'beş', 6: 'altı', 7: 'yedi', 8: 'sekiz', 9: 'dokuz'
    }
    tens_lookup_table = {10: 'on', 20: 'yirmi', 30: 'otuz', 40: 'kırk',
        50: 'elli', 60: 'altmış', 70: 'yetmiş', 80: 'seksen', 90: 'doksan'
    }
    ret = ''
    if num < 10:
        ret = ones_lookup_table[num]
    elif num % 10 != 0:
        ret = f'{tens_lookup_table[num - num % 10]} {ones_lookup_table[num % 10]}'
    else:
        ret = tens_lookup_table[num - num % 10]
    return ret
