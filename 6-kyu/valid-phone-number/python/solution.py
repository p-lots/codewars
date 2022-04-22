def valid_phone_number(phone_number):
    return len(phone_number) == 14 and phone_number[0] == '(' and phone_number[4] == ')' \
        and phone_number[5] == ' ' and phone_number[9] == '-' \
        and all(ch.isdigit() for ch in phone_number[1:4]) \
        and all(ch.isdigit() for ch in phone_number[6:9]) \
        and all(ch.isdigit() for ch in phone_number[11:])
