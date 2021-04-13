def alias_gen(f_name, l_name):
    return f'{FIRST_NAME[f_name[0].upper()]} {SURNAME[l_name[0].upper()]}' if f_name[0].isalpha() and l_name[0].isalpha() else 'Your name must start with a letter from A - Z.'
