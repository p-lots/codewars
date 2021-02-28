import re

def remove_bmw(strng):
    if type(strng) != str:
        return 'This program only works for text'
    return re.sub(r'[bmwBMW]', '', strng)