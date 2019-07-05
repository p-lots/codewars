def get_issuer(number):
    number = str(number)
    if number[:2] == '34' or number[:2] == '37' and len(number) == 15:
        return 'AMEX'
    elif number[:4] == '6011' and len(number) == 16:
        return 'Discover'
    elif 55 >= int(number[:2]) >= 50 and len(number) == 16:
        return 'Mastercard'
    elif number[0] == '4' and (len(number) == 13 or len(number) == 16):
        return 'VISA'
    else:
        return 'Unknown'