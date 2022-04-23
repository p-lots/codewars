LOOKUP = {'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5', 'F': '6', 'G': '7', 'H': '8',
             'J': '1', 'K': '2', 'L': '3', 'M': '4', 'N': '5', 'P': '7', 'R': '9', 'S': '2',
             'T': '3', 'U': '4', 'V': '5', 'W': '6', 'X': '7', 'Y': '8', 'Z': '9'}

VALID_CHARS = 'ABCDEFGHJKLMNPRSTUVWXYZ0123456789'

WEIGHTS = [8, 7, 6, 5, 4, 3, 2, 10, 0, 9, 8, 7, 6, 5, 4, 3, 2]
    

def is_valid_vin(number):
    return all(n in VALID_CHARS for n in number) and len(number) == 17

def check_vin(number):
    if not is_valid_vin(number):
        return False
    decoded = [int(LOOKUP.get(num, num)) for num in list(number)]
    checksum = sum(num * weight for num, weight in zip(decoded, WEIGHTS))
    checksum_mod_eleven = checksum % 11
    return str(checksum_mod_eleven) == number[8] or checksum_mod_eleven == 10 and number[8] == 'X'
