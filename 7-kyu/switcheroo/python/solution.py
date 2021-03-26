def switcheroo(strng):
    trans_table = str.maketrans('ab', 'ba')
    return strng.translate(trans_table)
