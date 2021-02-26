import re

def validate_pin(pin):
    if pin and pin[-1] == '\n':
        return False
    return True if re.match(r'^\d{4}$', pin) or re.match(r'^\d{6}$', pin) else False