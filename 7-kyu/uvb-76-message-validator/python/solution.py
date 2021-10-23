def validate(message):
    msg_split = message.split()
    if len(msg_split) != 8:
        return False
    has_initial_keyword = msg_split[0] == 'MDZHB'
    has_first_group_of_digits = msg_split[1].isdigit() and msg_split[2].isdigit() and \
        len(msg_split[1]) == 2 and len(msg_split[2]) == 3
    has_uppercase_keyword = msg_split[3].isupper() and all(ch.isalpha() for ch in msg_split[3])
    has_final_group_of_digits = True
    for i in range(4, 8):
        has_final_group_of_digits = has_final_group_of_digits and (msg_split[i].isdigit() and len(msg_split[i]) == 2)
    return has_initial_keyword and has_first_group_of_digits and has_uppercase_keyword and has_final_group_of_digits
